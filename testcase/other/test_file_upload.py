import allure

from pageObject.other.file_upload_page import FilesUploadPage


@allure.feature('文件上传')
class TestFilesUpload:

    @allure.story('成功上传文件')
    def test_file_upload_success(self, not_login_driver):
        fu = FilesUploadPage(not_login_driver)
        fu.files_upload()
        # 断言结果
        assert fu.get_tag_text(fu.assert_result) != ''
