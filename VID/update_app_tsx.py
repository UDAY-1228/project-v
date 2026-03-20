import os
import re

app_tsx_path = "/Users/nivas/Documents/React apps/v/project-v/VID/src/App.tsx"

workspaces = [
    "principal", "admission_officer", "admissions_counselor",
    "common", "team_owner", "employee", "hostel_admin",
    "payment_administrator", "faculty", "student"
]

with open(app_tsx_path, 'r') as f:
    content = f.read()

# Add imports for NoticeBoards for each workspace if not exists
imports_to_add = []
routes_to_add_dict = {}

for ws in workspaces:
    ws_path = ws.replace('_', '-')
    pascal_ws = ''.join(word.capitalize() for word in ws.split('_'))
    
    import_line = f"import {pascal_ws}NoticeBoard from '../workspaces/{ws}/frontend/pages/NoticeBoard';"
    route_line = f"        <Route path=\"/{ws_path}/notice-board\" element={{<{pascal_ws}NoticeBoard />}} />"
    
    if import_line not in content:
        imports_to_add.append(import_line)
    
    if route_line not in content:
        routes_to_add_dict[ws] = route_line

# Inject imports before `const App: React.FC = () => {`
if imports_to_add:
    import_index = content.find("const App: React.FC = () => {")
    content = content[:import_index] + "\n".join(imports_to_add) + "\n\n" + content[import_index:]

# Inject routes directly below their respective dashboard routes
for ws, route_line in routes_to_add_dict.items():
    ws_path = ws.replace('_', '-')
    search_route = f'<Route path="/{ws_path}/dashboard"'
    route_index = content.find(search_route)
    if route_index != -1:
        end_of_line = content.find("\n", route_index)
        content = content[:end_of_line] + "\n" + route_line + content[end_of_line:]

with open(app_tsx_path, 'w') as f:
    f.write(content)

print("Updated App.tsx with NoticeBoard links.")
