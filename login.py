import DecryptLogin

def login(username ,password):
  lg = login.Login()
  _,session = lg.music163(username,password)
  return session
def parseArgs():
  parser = argparse.ArgumentParser(description='网易云音乐自动签到')
  parser.add_argument('--username', dest='username', help='用户名', type=str, required=True)
  parser.add_argument('--password', dest='password', help='密码', type=str, required=True)
  args = parser.parse_args()
  return args

headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Referer': 'http://music.163.com/discover',
      'Accept': '*/*'
    }
csrf = re.findall('__csrf=(.*?) for', str(session.cookies))[0]
url = 'https://music.163.com/weapi/point/dailyTask?csrf_token=' + csrf
cracker = Cracker()
data = {
          'type': typeid
        }
data = cracker.get(data)
res = self.session.post(url, headers=headers, data=data)

if os.path.exists('config.json'):
  f = open('config.json', 'r', encoding='utf-8')
  info = json.load(f)
  f.close()
else:
  args = parseArgs()
  info = {'username': args.username, 'password': args.password}
  f = open('config.json', 'w', encoding='utf-8')
  json.dump(info, f)
  f.close()