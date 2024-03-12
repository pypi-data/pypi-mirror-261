import dataclasses
import datetime
import logging

import requests

from petersburgedu_wrap.types.action_payload import ActionPayload
from petersburgedu_wrap.types.estimate import Estimate
from petersburgedu_wrap.types.lesson_entry import LessonEntry
from petersburgedu_wrap.types.mark_entry import MarkEntry
from petersburgedu_wrap.types.task import Task
from petersburgedu_wrap.types.teacher import Teacher
from petersburgedu_wrap.types.identity import Identity
from petersburgedu_wrap.types.education import Education
from petersburgedu_wrap.utils import endpoints, request_parameters


@dataclasses.dataclass
class Child:
    """
    Class represents Children API entity
    :param firstname:
    :param surname:
    :param middlename:
    :param educations:
    :param action_payload:
    :param hash_uid:
    :param identity:
    :param token: JWT-Token for using methods
    """
    firstname: str
    middlename: str
    surname: str
    educations: list[Education]
    action_payload: ActionPayload
    hash_uid: str
    identity: Identity
    token: str

    def __post_init__(self) -> None:
        """
        Class represents Children API entity
        """
        self.logger = logging.getLogger("Child - %id%".replace("%id%", str(self.identity.id)))
        self.logger.debug("Child successfully created")
        self._token = self.token
        del self.token

    def get_teacher_list(self) -> list[Teacher]:
        """
        Function to get list of teachers of concrete student
        :return: List of teachers
        """
        education_id = self.educations[0].education_id
        self.logger.debug("Started request to get teacher list")
        teacher_list = []
        url = endpoints.TEACHER_LIST_URL.replace("{{page}}", "1").replace("{{education_id}}", str(education_id))
        payload = {}
        headers = request_parameters.headers
        cookies = {
            "X-JWT-Token": self._token
        }

        response = requests.request("GET", url, headers=headers, data=payload, cookies=cookies, timeout=1000)
        response_json = response.json()
        self.logger.debug(
            "Get the response to get teacher list with %code% status code".replace("%code%", str(response.status_code)))
        if response.status_code != 200:
            return []
        for teacher in response_json["data"]["items"]:
            firstname = teacher.get("firstname", "")
            surname = teacher.get("surname", "")
            middlename = teacher.get("middlename", "")
            position_name = teacher.get("position_name", "")
            subjects = teacher.get("subjects", "")
            teacher_list.append(Teacher(
                firstname=firstname,
                surname=surname,
                middlename=middlename,
                position_name=position_name,
                subjects=subjects
            ))
        return teacher_list

    def get_mark_list_by_period(self, date_from: datetime.date, date_to: datetime.date, education_number: int = 0) \
            -> list[MarkEntry]:
        """
        Function for getting mark list from API
        :param date_from:
        :param date_to:
        :param education_number:
        :return:
        """
        url = ((endpoints.MARKS_BY_DATE_URL
                .replace("{{education_id}}", str(self.educations[education_number].education_id))
                .replace("{{date_from}}", date_from.strftime("%d.%m.%Y")))
               .replace("{{date_to}}", date_to.strftime("%d.%m.%Y")))
        cookie = {"X-JWT-Token": self._token}
        headers = request_parameters.headers
        self.logger.debug("Data for get marks by period prepared")
        pages = []
        with requests.session() as session:
            response = session.request("GET", url.replace("{{page}}", "0"), cookies=cookie, headers=headers)
            self.logger.debug("Made request 1st page of marks with status code %code%"
                              .replace("%code%", str(response.status_code)))
            pages.append(response.json())

            if (total_pages := pages[0]["data"]["total_pages"]) > 1:
                for page_number in range(2, total_pages + 1):
                    response = session.request("GET", url.replace("{{page}}", str(page_number)), cookies=cookie,
                                               headers=headers)
                    pages.append(response.json())
                    self.logger.debug("Made request %page% page of marks with status code %code%"
                                      .replace("%code%", str(response.status_code)).replace("%page%", str(page_number)))
        marks = [MarkEntry(
            id=entry["id"],
            education_id=entry["education_id"],
            lesson_id=entry.get("lesson_id", 0),
            subject_id=entry["subject_id"],
            subject_name=entry["subject_name"],
            date=datetime.datetime.strptime(entry["date"], "%d.%m.%Y"),
            estimate_value_code=entry.get("estimate_value_code", ""),
            estimate_value_name=entry.get("estimate_value_name", ""),
            estimate_type_code=entry.get("estimate_type_code", ""),
            estimate_type_name=entry.get("estimate_type_name", ""),
            estimate_comment=entry.get("estimate_comment", ""))
            for page in pages
            for entry in page["data"]["items"]]
        return marks

    def get_lesson_list_by_period(self, date_from: datetime.date, date_to: datetime.date, education_number: int = 0) \
            -> list[LessonEntry]:
        """
        Function to get lessons by period
        :param date_from:
        :param date_to:
        :param education_number:
        :return:
        """
        pages = []
        url = (endpoints.LESSONS_BY_DATE_URL.replace("{{date_from}}", date_from.strftime("%d.%m.%Y"))
               .replace("{{date_to}}", date_to.strftime("%d.%m.%Y"))
               .replace("{{education_id}}", str(self.educations[education_number].education_id)))
        cookies = {
            "X-JWT-Token": self._token
        }
        self.logger.debug("Data for get lessons by period prepared")
        headers = request_parameters.headers
        with requests.session() as session:
            response = session.request("GET", url.replace("{{page}}", "0"), cookies=cookies, headers=headers)
            self.logger.debug("Made request 1st page of lessons with status code %code%"
                              .replace("%code%", str(response.status_code)))
            pages.append(response.json())
            if (total_pages := pages[0]["data"]["total_pages"]) > 1:
                for page_number in range(2, total_pages + 1):
                    response = session.request("GET", url.replace("{{page}}", str(page_number)), cookies=cookies,
                                               headers=headers)
                    pages.append(response.json())
                    self.logger.debug("Made request %page% page of lessons with status code %code%"
                                      .replace("%code%", str(response.status_code)).replace("%page%", str(page_number)))
        lessons = []
        for page in pages:
            for entry in page["data"]["items"]:
                tasks = []
                for task in entry["tasks"]:
                    files = task.get("files", [])
                    tasks.append(Task(task_name=task.get("task_name", ""),
                                      task_code=task.get("task_code", None),
                                      task_kind_code=task.get("task_kind_code", ""),
                                      task_kind_name=task.get("task_kind_name", ""),
                                      files=files))
                estimates = [Estimate(
                    estimate_type_code=estimate.get("estimate_type_code", ""),
                    estimate_type_name=estimate.get("estimate_type_name", ""),
                    estimate_value_code=estimate.get("estimate_value_code", ""),
                    estimate_value_name=estimate.get("estimate_value_name", ""),
                    estimate_comment=estimate.get("estimate_comment", None))
                    for estimate in entry["estimates"]]
                lessons.append(LessonEntry(
                    identity=Identity(entry["identity"]["id"], entry["identity"].get("uid", None)),
                    number=entry.get("number", 0),
                    datetime_from=datetime.datetime.strptime(entry.get("datetime_from", "01.01.1970"),
                                                             "%d.%m.%Y %H:%M:%S"),
                    datetime_to=datetime.datetime.strptime(entry.get("datetime_to", "01.01.1970"),
                                                           "%d.%m.%Y %H:%M:%S"),
                    subject_id=entry.get("subject_id", 0),
                    subject_name=entry.get("subject_name", ""),
                    content_name=entry.get("content_name", ""),
                    content_description=entry.get("content_description", None),
                    content_additional_material=entry.get("content_additional_material", ""),
                    tasks=tasks,
                    estimates=estimates,
                    action_payload=ActionPayload()
                ))
        return lessons
