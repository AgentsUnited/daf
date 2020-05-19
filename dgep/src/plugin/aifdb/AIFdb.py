import os
import json

class aifdb():

	def __init__(self):
		self.dialogue_id = 1
		self.get_methods = {"templates": self.get_templates}
		self.path = os.path.dirname(os.path.realpath(__file__))
		print("AIFdb plugin initialised")

	def invoke(self, data={}):
		if "moveID" in list(data.keys()):
			template = open(self.path + "/move_templates/" + data["moveID"] + ".aif", 'r').read()

			if "params" in list(data.keys()):
				params = data["params"]

				for key,value in params.items():
					template = template.replace("$" + key, value)

				#and here we update AIFdb...for later


	def update(self, params={}):
		if params["cmd"] == "new_template":
			data = params["params"]
			template = open(self.path + "/move_templates/" + data["name"] + ".aif", 'w+')

			template.write(data["content"])

			return {"msg":"Template for move " + data["name"] + " created"}
		elif params["cmd"] == "update_template":
			data = params["params"]
			template = open(self.path + "/move_templates/" + data["name"] + ".aif", 'w')

			template.write(json.dumps(data["content"]))

			return {"msg":"Template for move " + data["name"] + " updated"}

	def get_description(self):

		template = open(os.path.dirname(os.path.realpath(__file__)) + '/config/template.htm')

		return {"name":"AIFdb", "config_template":template.read()}

	def get(self, what):
		if what in list(self.get_methods.keys()):
			return self.get_methods[what]()

	def get_templates(self):
		templates = []
		templates_path = self.path + "/move_templates"

		for f in os.listdir(templates_path):
			if f.endswith(".aif"):
				template = open(templates_path + "/" + f, 'r')
				templates.append({"name": f[:-4], "template": template.read()})


		return {"templates":templates}

	def save(self):
		return {"dialogueID": self.dialogueID}
