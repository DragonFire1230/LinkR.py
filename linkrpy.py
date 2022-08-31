import requests

class ConnectError(Exception):
	pass

class LinkR():
	def __init__(self, key):
		self.key = key
		try:
			request = requests.get(f'https://linkr.repl.co/api/key/check?key={key}')

			if request.status_code == 200:
				pass
			else:
				raise ConnectError("We can't connect to LinkR. Please check your API Key, and try again.")
		except requests.exceptions.ConnectionError:
			raise ConnectError("LinkR down! We can't connect to LinkR.")

	def generate(self, url):
		request = requests.post(f'https://linkr.repl.co/api/generate', json = {
			"url": url,
			"key": self.key}
		)
		return request.json()['response']