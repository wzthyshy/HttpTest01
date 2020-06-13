import  requests


class TestHttp:
    # def test_get(self):
    #     import requests
    #     r = requests.get('https://home.testing-studio.com/t/topic/1682')
    #     print(r.status_code)
    #     print(r.text)
    #
    #     assert r.status_code==200
    # def test_query(self):
    #     r=requests.get(
    #         'https://home.testing-studio.com/search',
    #         params={'q':'requests'}
    #                    )
    #     print(r.text)
    #     assert r.status_code==200
    #
    # def test_form(self):
    #     r=requests.post('http://user.cdlmwx.com/chedaiunion/newcomlist',
    #                     data={
    #                         'phoneno':'15268632902',
    #                         'password':'1234567',
    #                         'fphonemeid':'b04c61d7-1307-38c8-84c8-ac0597b0d822'
    #                     }
    #                     )
    #     print(r.status_code)
    #     print(r.text)

    def test_json(self):
        r=requests.post('http://user.cdlmwx.com/chedaiunion/newcomlist',
                        data={
                            'phoneno':'15268632902',
                            'password':'1234567',
                            'fphonemeid':'b04c61d7-1307-38c8-84c8-ac0597b0d822'
                        }
                        )
        print(r.json())

        # assert r.json()['msg']=='成功!'
        assert r.json()['retCode']=='0000'




