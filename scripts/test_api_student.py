import datetime
import random
import time
import unittest
from urllib.parse import urlencode
import requests
import my_variable

base_url = "https://sitcmsapi.apfeg.com"


class TestApiStudent(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # 获取验证码接口
    def test_a_get_code(self):
        """获取验证码接口"""
        url_a = base_url + "/Api/Captcha/getCaptcha"

        try:
            reply_1 = requests.post(url=url_a)
            assert 200 == reply_1.status_code
        except:
            print("接口1：获取验证码，失败")
            raise
        else:
            print("接口1：获取验证码，成功")
            my_variable.captcha_key = reply_1.json()["data"]["captchaKey"]

    # 登录接口
    def test_b_login(self):
        """登录接口"""
        try:
            json_b1 = {
                "userName": "HNXX0S202002003",
                "password": "abc12345~",
                "captchaKey": my_variable.captcha_key,
                "remember": False,
                "clientAppType": 0
            }
            url_b1 = base_url + "/Api/Login?" + urlencode(json_b1)
            try:
                reply_b1 = requests.post(url=url_b1)
                assert "登录成功" in reply_b1.json()["message"]
            except:
                print("接口2：学生账号登录，失败")
                raise
            else:
                print("接口2：学生账号登录，成功")
                my_variable.access_token = "Bearer " + reply_b1.json()["accessToken"]
                my_variable.user_id = reply_b1.json()["data"]["userId"]
                my_variable.unit_session_uid = reply_b1.json()["data"]["unit_session_uid"]
                my_variable.uni_id = reply_b1.json()["data"]["unitId"]

            # 获取学生信息
            header_b2 = {
                        "Content-Type": "application/json;charset=utf-8",
                        "Authorization": my_variable.access_token
                        }
            json_b2 = {
                "userId": my_variable.user_id
            }
            url_b2 = base_url + "/Api/Login/GetUserInfo?" + urlencode(json_b2)
            try:
                reply_b2 = requests.post(url=url_b2, headers=header_b2)
                assert "查询成功" in reply_b2.json()["message"]
            except:
                print("接口3：获取学生信息，失败")
                raise
            else:
                print("接口3：获取学生信息，成功")
        except:
            raise

    # 首页模块接口
    def test_c_homepage(self):
        """首页模块接口"""
        header_c = {
            "Content-Type": "application/json;charset=utf-8",
            "Authorization": my_variable.access_token
        }

        try:
            # 首页-获取任务单、表扬、微课和错题数据
            json_c1 = {
                "per_id": my_variable.user_id
            }
            url_c1 = base_url + "/Api/ResourceStatistics/CountStudentMessage?" + urlencode(json_c1)
            try:
                reply_c1 = requests.post(url=url_c1, headers=header_c)
                assert "取得信息成功" in reply_c1.json()["message"]
            except:
                print("接口4：首页-获取任务单、表扬、微课和错题数据，失败")
                raise
            else:
                print("接口4：首页-获取任务单、表扬、微课和错题数据，成功")

            # 首页-获取课表信息
            json_c2 = {
                "per_id": my_variable.user_id
            }
            url_c2 = base_url + "/Api/ResourceStatistics/StudentCourseSchedule?" + urlencode(json_c2)
            try:
                reply_c2 = requests.post(url=url_c2, headers=header_c)
                assert "取得信息成功" in reply_c2.json()["message"]
            except:
                print("接口5：首页-获取课表信息，失败")
                raise
            else:
                print("接口5：首页-获取课表信息，成功")

            # 首页-获取成绩趋势
            json_c3 = {
                "per_id": my_variable.user_id,
                "timetype": 1
            }
            url_c3 = base_url + "/Api/Examination/ShowMyPerformanceTrends?" + urlencode(json_c3)
            try:
                reply_c3 = requests.post(url=url_c3, headers=header_c)
                assert "暂无信息" in reply_c3.json()["message"]
            except:
                print("接口6：首页-获取成绩趋势，失败")
                raise
            else:
                print("接口6：首页-获取成绩趋势，成功")

            # 首页-获取班级风采
            json_c4 = {
                "per_id": my_variable.user_id
            }
            url_c4 = base_url + "/Api/Classes/ClassStyle?" + urlencode(json_c4)
            try:
                reply_c4 = requests.post(url=url_c4, headers=header_c)
                assert "暂无信息" in reply_c4.json()["message"]
            except:
                print("接口7：首页-获取班级风采，失败")
                raise
            else:
                print("接口7：首页-获取班级风采，成功")

            # 首页-获取被表扬次数
            url_c5 = "https://sitapplethomeschool.apfeg.com/api/StudentOfHomeSchool/GetStudentPraise"
            try:
                reply_c5 = requests.post(url=url_c5, headers=header_c)
                assert 200 == reply_c5.status_code
            except:
                print("接口8：首页-获取被表扬次数，失败")
                raise
            else:
                print("接口8：首页-获取被表扬次数，成功")

            # 首页-获取分数排名
            url_c6 = "https://sitapplethomeschool.apfeg.com/api/StudentOfHomeSchool/GetScoreRanking"
            try:
                reply_c6 = requests.post(url=url_c6, headers=header_c)
                assert "学生" in reply_c6.text
            except:
                print("接口9：首页-获取分数排名，失败")
                raise
            else:
                print("接口9：首页-获取分数排名，成功")

            # 首页-获取主观评价
            url_c7 = "https://sitapplethomeschool.apfeg.com/api/StudentOfHomeSchool/GetMySubjectiveEvaluation?timetype=1"
            try:
                reply_c7 = requests.post(url=url_c7, headers=header_c)
                assert 200 == reply_c7.status_code
            except:
                print("接口10：首页-获取主观评价，失败")
                raise
            else:
                print("接口10：首页-获取主观评价，成功")
        except:
            raise

    # 学生个人空间模块接口
    def test_d_person_space(self):
        """学生个人空间模块接口"""
        header_d = {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authorization": my_variable.access_token
                }

        try:
            # 个人空间-获取个人空间信息
            data_d1 = {
                "per_id": my_variable.user_id
            }
            url_d1 = base_url + "/api/Space/GetSeSpaceByPerId?" + urlencode(data_d1)
            try:
                reply_d1 = requests.post(url=url_d1, headers=header_d)
                assert "暂无数据" in reply_d1.json()["message"]
            except:
                print("接口11：个人空间-获取个人空间信息，失败")
                raise
            else:
                print("接口11：个人空间-获取个人空间信息，成功")

            # 个人空间-获取个人简介信息
            data_d2 = {
                "per_id": my_variable.user_id,
                "per_desc": ""
            }
            url_d2 = base_url + "/Api/Personnel/GetPersonnelProfileByPerId?" + urlencode(data_d2)
            try:
                reply_d2 = requests.post(url=url_d2, headers=header_d)
                assert "获取简介" in reply_d2.json()["message"]
            except:
                print("接口12：个人空间-获取个人简介信息，失败")
                raise
            else:
                print("接口12：个人空间-获取个人简介信息，成功")

            # 个人空间-修改个人简介信息
            data_d3 = {
                "page": 1,
                "pageSize": 20,
                "per_id": my_variable.user_id,
                "per_desc": "jmeter-test" + str(random.randint(1, 10))
            }
            url_d3 = base_url + "/Api/Personnel/UpdatepersonnelProfile?" + urlencode(data_d3)
            try:
                reply_d3 = requests.post(url=url_d3, headers=header_d)
                assert "修改简介成功" in reply_d3.json()["message"]
            except:
                print("接口13：个人空间-修改个人简介信息，失败")
                raise
            else:
                print("接口13：个人空间-修改个人简介信息，成功")

            # 个人空间-新增日志
            data_d4 = {
                "se_dirary_title": "python自动化学生日志标题" + str(random.randint(1, 10)),
                "se_dirary_content": "python自动化学生日志内容" + str(random.randint(1, 10)),
                "se_dirary_uid": "",
                "user_id": my_variable.user_id,
                "per_id": my_variable.user_id
            }
            cdate = time.strftime("%Y-%m-%d+%H:%M:%S")
            url_d4 = base_url + "/api/Space/InsertOrUpdateSeDirary?" + urlencode(data_d4) + "&cdate=" + cdate
            try:
                reply_d4 = requests.post(url=url_d4, headers=header_d)
                assert "添加或修改个人日志成功" in reply_d4.json()["message"]
            except:
                print("接口14：个人空间-新增日志，失败")
                raise
            else:
                print("接口14：个人空间-新增日志，成功")
                my_variable.se_dirary_title = data_d4["se_dirary_title"]
                my_variable.se_dirary_content = data_d4["se_dirary_content"]
                my_variable.se_dirary_cdate = cdate

            # 个人空间-获取个人日志信息
            data_d5 = {
                "page": 1,
                "pageSize": 20,
                "per_id": my_variable.user_id
            }
            url_d5 = base_url + "/api/Space/GetSeDiraryByPerId?" + urlencode(data_d5)
            try:
                reply_d5 = requests.post(url=url_d5, headers=header_d)
                assert "查询个人日志成功" in reply_d5.json()["message"]
            except:
                print("接口15：个人空间-获取个人日志信息，失败")
                raise
            else:
                print("接口15：个人空间-获取个人日志信息，成功")
                my_variable.se_dirary_uid = reply_d5.json()["data"]["list"][0]["se_dirary_uid"]

            # 个人空间-删除个人日志
            data_d6 = {
                "se_dirary_title": my_variable.se_dirary_title,
                "se_dirary_content": my_variable.se_dirary_content,
                "se_dirary_uid": my_variable.se_dirary_uid,
                "per_id": my_variable.user_id
            }
            url_d6 = base_url + "/api/Space/DeleteSeDirary?" + urlencode(data_d6) + "&cdate=" + my_variable.se_dirary_cdate
            try:
                reply_d6 = requests.post(url=url_d6, headers=header_d)
                assert "删除个人日志成功" in reply_d6.json()["message"]
            except:
                print("接口16：个人空间-删除个人日志，失败")
                raise
            else:
                print("接口16：个人空间-删除个人日志，成功")

            # 个人空间-获取科目正确率
            data_d7 = {
                "per_id": my_variable.user_id
            }
            url_d7 = base_url + "/api/GuideLearnStudent/SubjectAccuracy?" + urlencode(data_d7)
            try:
                reply_d7 = requests.post(url=url_d7, headers=header_d)
                assert "查询成功" in reply_d7.json()["message"]
            except:
                print("接口17：个人空间-获取科目正确率，失败")
                raise
            else:
                print("接口17：个人空间-获取科目正确率，成功")

            # 个人空间-获取学段信息
            url_d8 = base_url + "/Api/Subject/GetSectionDrop"
            try:
                reply_d8 = requests.post(url=url_d8, headers=header_d)
                assert "查询成功" in reply_d8.json()["message"]
            except:
                print("接口18：个人空间-获取学段信息，失败")
                raise
            else:
                print("接口18：个人空间-获取学段信息，成功")
                # 提取小学学段ID
                my_variable.sec_id = reply_d8.json()["data"][0]["sec_id"]

            # 个人空间-获取科目
            data_d9 = {
                "sec_id": my_variable.sec_id
            }
            url_d9 = base_url + "/Api/Subject/GetSubjectDrop?" + urlencode(data_d9)
            try:
                reply_d9 = requests.post(url=url_d9, headers=header_d)
                assert "查询成功" in reply_d9.json()["message"]
            except:
                print("接口19：个人空间-获取科目，失败")
                raise
            else:
                print("接口19：个人空间-获取科目，成功")
                # 提取小学语文科目ID
                my_variable.sub_id = reply_d9.json()["data"][44]["sub_id"]

            # 个人空间-获取默认学段
            url_d10 = base_url + "/api/GuideLearnStudent/GetMySecName"
            try:
                reply_d10 = requests.post(url=url_d10, headers=header_d)
                assert "获取学段名称信息成功" in reply_d10.json()["message"]
            except:
                print("接口20：个人空间-获取默认学段，失败")
                raise
            else:
                print("接口20：个人空间-获取默认学段，成功")

            # 个人空间-添加读书笔记
            url_d11 = base_url + "/api/GuideLearnStudent/AddUserReadingNote"
            json_d11 = {
                        "content_file_id": "<p> python读书笔记内容</p>",
                        "create_user_id": my_variable.user_id,
                        "note_title": "python读书笔记标题" + str(random.randint(1, 100)),
                        "sec_id": my_variable.sec_id,
                        "sub_id": my_variable.sub_id
                    }
            try:
                reply_d11 = requests.post(url=url_d11, json=json_d11, headers=header_d)
                assert "添加或者修改读书笔记信息成功" in reply_d11.json()["message"]
            except:
                print("接口21：个人空间-添加读书笔记，失败")
                raise
            else:
                print("接口21：个人空间-添加读书笔记，成功")

            # 个人空间-获取列表读书笔记数据
            data_d12 = {
                        "pageIndex": 1,
                        "pageSize": 20,
                        "sec_id": my_variable.sec_id,
                        "sub_id": my_variable.sub_id,
                        "per_id": my_variable.user_id
                    }
            url_d12 = base_url + "/api/GuideLearnStudent/GetMyReadingNote?" + urlencode(data_d12)
            try:
                reply_d12 = requests.post(url=url_d12, headers=header_d)
                assert "查询成功" in reply_d12.json()["message"]
            except:
                print("接口22：个人空间-获取列表读书笔记数据，失败")
                raise
            else:
                print("接口22：个人空间-获取列表读书笔记数据，成功")
                # 提取要删除的读书笔记的ID
                my_variable.note_id = reply_d12.json()["data"]["list"][0]["id"]

            # 个人空间-删除读书笔记
            data_d13 = {
                        "per_id": my_variable.user_id,
                        "id": my_variable.note_id
                    }
            url_d13 = base_url + "/api/GuideLearnStudent/DeleteUserReadingNote?" + urlencode(data_d13)
            try:
                reply_d13 = requests.post(url=url_d13, headers=header_d)
                assert "删除读书笔记信息成功" in reply_d13.json()["message"]
            except:
                print("接口23：个人空间-删除读书笔记，失败")
                raise
            else:
                print("接口23：个人空间-删除读书笔记，成功")

            # 个人空间-获取课程
            data_d14 = {
                        "unit_session_uid": my_variable.unit_session_uid,
                        "per_id": my_variable.user_id
                    }
            url_d14 = base_url + "/api/GuideLearnStudent/StudentCurriculumDrop?" + urlencode(data_d14)
            try:
                reply_d14 = requests.post(url=url_d14, headers=header_d)
                assert "查询成功" in reply_d14.json()["message"]
            except:
                print("接口24：个人空间-获取课程，失败")
                raise
            else:
                print("接口24：个人空间-获取课程，成功")
                # 提取一年级1班语文的课程ID
                my_variable.cou_id = reply_d14.json()["data"][0]["cou_id"]

            # 个人空间-获取错题集列表数据
            data_d15 = {
                        "pageIndex": 1,
                        "pageSize": 20,
                        "per_id": my_variable.user_id,
                        "cou_id": my_variable.cou_id
                    }
            url_d15 = base_url + "/api/GuideLearnStudent/GetWrongQuetionByCouId?" + urlencode(data_d15)
            try:
                reply_d15 = requests.post(url=url_d15, headers=header_d)
                assert "查询错题本列表信息成功" in reply_d15.json()["message"]
            except:
                print("接口25：个人空间-获取错题集列表数据，失败")
                raise
            else:
                print("接口25：个人空间-获取错题集列表数据，成功")

            # 个人空间-获取任务单正确率
            data_d16 = {
                        "per_id": my_variable.user_id,
                        "type": "x"
                    }
            url_d16 = base_url + "/api/GuideLearnStudent/GuideLearnAccuracy?" + urlencode(data_d16)
            try:
                reply_d16 = requests.post(url=url_d16, headers=header_d)
                assert "查询成功" in reply_d16.json()["message"]
            except:
                print("接口26：个人空间-获取任务单正确率，失败")
                raise
            else:
                print("接口26：个人空间-获取任务单正确率，成功")

            # 个人空间-获取待加强知识点
            data_d17 = {
                        "per_id": my_variable.user_id,
                        "cou_id": my_variable.cou_id,
                        "unit_session_uid": my_variable.unit_session_uid,
                        "type": "x"
                    }
            url_d17 = base_url + "/api/GuideLearnStudent/StrengthenKnowledgePoints?" + urlencode(data_d17)
            try:
                reply_d17 = requests.post(url=url_d17, headers=header_d)
                assert "查询成功" in reply_d17.json()["message"]
            except:
                print("接口27：个人空间-获取待加强知识点，失败")
                raise
            else:
                print("接口27：个人空间-获取待加强知识点，成功")

            # 个人空间-添加日记
            # 获取今天是星期几
            day_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
            what_today = datetime.datetime.now().weekday()
            to_today = day_list[what_today]

            json_d18 = {
                          "id": 0,
                          "happenDate": time.strftime("%Y-%m-%d") + "T16:00:00.000Z",
                          "week": to_today,
                          "theWeather": "晴",
                          "diaryContent": "python添加日记" + str(random.randint(1, 100)),
                          "createTime": "",
                          "modifyTime": ""
                    }
            url_d18 = "https://sitapplethomeschool.apfeg.com/api/StudentOfHomeSchool/CreatEditDiary"
            try:
                reply_d18 = requests.post(url=url_d18, json=json_d18, headers=header_d)
                assert 200 == reply_d18.status_code
            except:
                print("接口28：个人空间-添加日记，失败")
                raise
            else:
                print("接口28：个人空间-添加日记，成功")

            # 个人空间-获取列表日记数据
            json_d19 = {
                        "page": 1,
                        "pageSize": 20
                    }
            url_d19 = "https://sitapplethomeschool.apfeg.com/api/StudentOfHomeSchool/GetDiaryListForESB"
            try:
                reply_d19 = requests.post(url=url_d19, json=json_d19, headers=header_d)
                assert 200 == reply_d19.status_code
            except:
                print("接口29：个人空间-获取列表日记数据，失败")
                raise
            else:
                print("接口29：个人空间-获取列表日记数据，成功")
                # 提取要删除的日记ID
                my_variable.diary_id = reply_d19.json()["data"]["rows"][0]["id"]

            # 个人空间-删除日记
            json_d20 = [my_variable.diary_id]
            url_d20 = "https://sitapplethomeschool.apfeg.com/api/StudentOfHomeSchool/DeleteDiary"
            try:
                reply_d20 = requests.post(url=url_d20, json=json_d20, headers=header_d)
                assert 200 == reply_d20.status_code
            except:
                print("接口30：个人空间-删除日记，失败")
                raise
            else:
                print("接口30：个人空间-删除日记，成功")
        except:
            raise

    # 学生学习计划模块接口
    def test_e_study_plan(self):
        """学生学习计划模块接口"""
        header_e = {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authorization": my_variable.access_token
                }

        try:
            # 学习计划-获取课前预习各总数数据
            data_e1 = {
                        "glaStatus": 1
                    }
            url_e1 = base_url + "/Api/StudentIndex/StudentStudyCount?" + urlencode(data_e1)
            try:
                reply_e1 = requests.post(url=url_e1, headers=header_e)
                assert "查询信息成功" in reply_e1.json()["message"]
            except:
                print("接口31：学习计划-获取课前预习各总数数据，失败")
                raise
            else:
                print("接口31：学习计划-获取课前预习各总数数据，成功")

            # 学习计划-获取课前科目信息
            url_e2 = base_url + "/Api/StudentIndex/GetCourseSubjectList"
            try:
                reply_e2 = requests.post(url=url_e2, headers=header_e)
                assert "查询信息成功" in reply_e2.json()["message"]
            except:
                print("接口32：学习计划-获取科目信息，失败")
                raise
            else:
                print("接口32：学习计划-获取科目信息，成功")

            # 学习计划-获取课前预习列表数据
            data_e3 = {
                        "subId": my_variable.sub_id,
                        "glaStatus": 1,
                        "pageIndex": 1,
                        "pageSize": 20
                    }
            url_e3 = base_url + "/Api/StudentIndex/StudentStudyList?" + urlencode(data_e3)
            try:
                reply_e3 = requests.post(url=url_e3, headers=header_e)
                assert "查询信息成功" in reply_e3.json()["message"]
            except:
                print("接口33：学习计划-获取课前预习列表数据，失败")
                raise
            else:
                print("接口33：学习计划-获取课前预习列表数据，成功")

            # 学习计划-获取课后学习各总数数据
            data_e4 = {
                        "glaStatus": 3
                    }
            url_e4 = base_url + "/Api/StudentIndex/StudentStudyCount?" + urlencode(data_e4)
            try:
                reply_e4 = requests.post(url=url_e4, headers=header_e)
                assert "查询信息成功" in reply_e4.json()["message"]
            except:
                print("接口34：学习计划-获取课后学习各总数数据，失败")
                raise
            else:
                print("接口34：学习计划-获取课后学习各总数数据，成功")

            # 学习计划-获取课后科目信息
            url_e5 = base_url + "/Api/StudentIndex/GetCourseSubjectList"
            try:
                reply_e5 = requests.post(url=url_e5, headers=header_e)
                assert "查询信息成功" in reply_e5.json()["message"]
            except:
                print("接口35：学习计划-获取课后科目信息，失败")
                raise
            else:
                print("接口35：学习计划-获取课后科目信息，成功")

            # 学习计划-获取课后预习列表数据
            data_e6 = {
                        "subId": my_variable.sub_id,
                        "glaStatus": 3,
                        "pageIndex": 1,
                        "pageSize": 20
                    }
            url_e6 = base_url + "/Api/StudentIndex/StudentStudyList?" + urlencode(data_e6)
            try:
                reply_e6 = requests.post(url=url_e6, headers=header_e)
                assert "查询信息成功" in reply_e6.json()["message"]
            except:
                print("接口36：学习计划-获取课后学习列表数据，失败")
                raise
            else:
                print("接口36：学习计划-获取课后学习列表数据，成功")

            # 学习计划-获取学习计划列表数据
            json_e7 = {
                        "type": 0,
                        "pageIndex": 1,
                        "pageSize": 20
                    }
            url_e7 = "https://sitstudenttablet.apfeg.com/api/StudentStudyPlan/GetMyStudentAplanEsb"
            try:
                reply_e7 = requests.post(url=url_e7, json=json_e7, headers=header_e)
                assert 200 == reply_e7.status_code
            except:
                print("接口37：学习计划-获取学习计划列表数据，失败")
                raise
            else:
                print("接口37：学习计划-获取学习计划列表数据，成功")
        except:
            raise

    # 学生作业模块接口
    def test_f_student_task(self):
        """学生作业模块接口"""
        header_f = {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authorization": my_variable.access_token
                }

        try:
            # 作业-获取全部、未完成、已完成作业列表数据
            url_f1 = base_url + "/api/RedesignGuideLearn/GetStudentGuideLearningList"
            for num in ["", 0, 1]:
                json_f1 = {
                            "gName": "",
                            "subId": my_variable.sub_id,
                            "glcChecked": num,
                            "pageIndex": 1,
                            "pageSize": 20
                        }
                try:
                    reply_f1 = requests.post(url=url_f1, json=json_f1, headers=header_f)
                    assert 200 == reply_f1.status_code
                except:
                    if num == "":
                        print("接口38：作业-获取全部作业列表数据，失败")
                    elif num == 0:
                        print("接口39：作业-获取未完成作业列表数据，失败")
                    elif num == 1:
                        print("接口40：作业-获取已完成作业列表数据，失败")
                    raise
                else:
                    if num == "":
                        print("接口38：作业-获取全部作业列表数据，成功")
                    elif num == 0:
                        print("接口39：作业-获取未完成作业列表数据，成功")
                    elif num == 1:
                        print("接口40：作业-获取已完成作业列表数据，成功")
        except:
            raise

    # 学生日常成绩模块接口
    def test_g_daily_score(self):
        """学生日常成绩模块接口"""
        header_g = {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authorization": my_variable.access_token
                }

        try:
            # 日常成绩-获取每次考试信息
            data_g1 = {
                        "uni_id": my_variable.uni_id,
                        "uni_session_uid": my_variable.unit_session_uid
                    }
            url_g1 = base_url + "/Api/Examination/GetExamListForSession?" + urlencode(data_g1)
            try:
                reply_g1 = requests.post(url=url_g1, headers=header_g)
                assert "查询信息成功" in reply_g1.json()["message"]
            except:
                print("接口41：日常成绩-获取每次考试信息，失败")
                raise
            else:
                print("接口41：日常成绩-获取每次考试信息，成功")
                # 提取最新一次的考试ID
                my_variable.ttm_id = reply_g1.json()["data"][0]["ttm_id"]

            # 日常成绩-单次测验成绩
            data_g2 = {
                        "per_id": my_variable.user_id,
                        "ttm_id": my_variable.ttm_id,
                        "uni_session_uid": my_variable.unit_session_uid
                    }
            url_g2 = base_url + "/Api/Examination/ResultsOfSingleSubject?" + urlencode(data_g2)
            try:
                reply_g2 = requests.post(url=url_g2, headers=header_g)
                assert "查询信息成功" in reply_g2.json()["message"]
            except:
                print("接口42：日常成绩-单次测验成绩，失败")
                raise
            else:
                print("接口42：日常成绩-单次测验成绩，成功")
        except:
            raise

    # 学生课堂学情模块接口
    def test_h_class_situation(self):
        """学生课堂学情模块接口"""
        header_h = {
                    "Content-Type": "application/json;charset=utf-8",
                    "Authorization": my_variable.access_token
                }

        try:
            # 课堂学情-获取每次测验成绩
            # s_time = datetime.datetime.now()
            # start_time = s_time.strftime("%Y-%m-%d")  # 开始时间
            # e_time = s_time + datetime.timedelta(days=30)
            # end_time = e_time.strftime("%Y-%m-%d")  # 结束时间
            data_h1 = {
                        "cou_id": my_variable.cou_id,
                        "startTime": "2020-07-01",
                        "endTime": "2021-07-01"
                    }
            url_h1 = base_url + "/Api/IRSRecord/GetTimeInterval?" + urlencode(data_h1)
            try:
                reply_h1 = requests.post(url=url_h1, headers=header_h)
                assert "操作成功" in reply_h1.json()["message"]
            except:
                print("接口43：课堂学情-获取每次测验成绩，失败")
                raise
            else:
                print("接口43：课堂学情-获取每次测验成绩，成功")
                # 提取最近一次测验的ID
                my_variable.irsr_id = reply_h1.json()["data"][0]["irsr_id"]

            # 课堂学情-我的测验情况
            data_h2 = {
                        "cou_id": my_variable.cou_id,
                        "irsr_id": my_variable.irsr_id,
                        "per_id": my_variable.user_id
                    }
            url_h2 = base_url + "/Api/IRSRecord/GetMyTestSituation?" + urlencode(data_h2)
            try:
                reply_h2 = requests.post(url=url_h2, headers=header_h)
                assert "操作成功" in reply_h2.json()["message"]
            except:
                print("接口44：课堂学情-我的测验情况，失败")
                raise
            else:
                print("接口44：课堂学情-我的测验情况，成功")

            # 课堂学情-我的学习分析
            data_h3 = {
                        "irsr_id": my_variable.irsr_id,
                        "per_id": my_variable.user_id
                    }
            url_h3 = base_url + "/Api/IRSRecord/GetMyLearningAnalysis?" + urlencode(data_h3)
            try:
                reply_h3 = requests.post(url=url_h3, headers=header_h)
                assert "操作成功" in reply_h3.json()["message"]
            except:
                print("接口45：课堂学情-我的学习分析，失败")
                raise
            else:
                print("接口45：课堂学情-我的学习分析，成功")

            # 课堂学情-我的答题分析
            data_h4 = {
                        "irsr_id": my_variable.irsr_id,
                        "per_id": my_variable.user_id
                    }
            url_h4 = base_url + "/Api/IRSRecord/GetMyAnswerAnalysis?" + urlencode(data_h4)
            try:
                reply_h4 = requests.post(url=url_h4, headers=header_h)
                assert "操作成功" in reply_h4.json()["message"]
            except:
                print("接口46：课堂学情-我的答题分析，失败")
                raise
            else:
                print("接口46：课堂学情-我的答题分析，成功")

            # 课堂学情-历次测验成绩
            data_h5 = {
                        "cou_id": my_variable.cou_id,
                        "per_id": my_variable.user_id,
                        "startTime": "2020-07-01",
                        "endTime": "2021-07-01"
                    }
            url_h5 = base_url + "/Api/IRSRecord/GetHistoryTest?" + urlencode(data_h5)
            try:
                reply_h5 = requests.post(url=url_h5, headers=header_h)
                assert "操作成功" in reply_h5.json()["message"]
            except:
                print("接口47：课堂学情-历次测验成绩，失败")
                raise
            else:
                print("接口47：课堂学情-历次测验成绩，成功")
        except:
            raise





