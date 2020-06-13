import requests

from HttpTest01.api import Wework, ExContact


class Testwork:
    @classmethod
    def setup_class(cls):
        cls.wework=Wework()
        cls.wework.get_token()
        cls.excontact=ExContact()

    def test_get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid': 'wwd6da61649bd66fea',
                'corpsecret': 'heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0'
            }
        )
        print(r.json())
        assert r.status_code == 200
        Wework.token = r.json()['access_token']

        # 获取客户列表
    def test_list(self):
        r=self.excontact.list('sihan')
        assert len(r.json()['external_userid'])>43

        uid=r.json()['external_userid'][0]


        r=requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get',
            params={
                'access_token':Wework.token,
                'external_userid':uid
            }
        )

        print(r.json())
        assert r.status_code==200