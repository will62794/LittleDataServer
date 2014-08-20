import Asana
asana_api = Asana.AsanaAPI('3D31plGb.tYIr08vhXQI3GEE8XgGm3AG', debug=True)

# see your workspaces
myspaces = asana_api.list_workspaces()  #Result: [{u'id': 123456789, u'name': u'asanapy'}]
workspace_id=myspaces[0]["id"]
print workspace_id


all_projects = asana_api.list_projects(workspace=workspace_id,include_archived=False)  #Result: [{u'id': 123456789, u'name': u'asanapy'}]

for project in all_projects:
	print project["name"]


project_tasks=asana_api.get_project_tasks(all_projects[1]["id"],include_archived=False)

for task in project_tasks:
	print task