import os
import re

workspaces = [
    "principal", "academic_coordinator", "admission_officer", "admissions_counselor",
    "common", "team_owner", "transport_coordinator", "employee", "hostel_admin",
    "payment_administrator", "examination", "faculty", "student"
]

base_dir = "/Users/nivas/Documents/React apps/v/project-v/VID/workspaces"

notice_board_string = """    {{
        "label": "Digital Notice Board",
        "icon": "announcement",
        "path": "/{ws_path}/notice-board"
    }},
"""

notice_board_component = """import React from 'react';
import SharedNoticeBoard from '../../../../core/frontend/pages/NoticeBoard';

const NoticeBoard: React.FC = () => {
    const sidebarItems = [
{sidebar_items_content}    ];

    return <SharedNoticeBoard sidebarItems={sidebarItems} />;
};

export default NoticeBoard;
"""

app_tsx_path = "/Users/nivas/Documents/React apps/v/project-v/VID/src/App.tsx"

for ws in workspaces:
    ws_path = ws.replace('_', '-')
    
    dashboard_path = os.path.join(base_dir, ws, "frontend/pages/Dashboard.tsx")
    notice_board_path = os.path.join(base_dir, ws, "frontend/pages/NoticeBoard.tsx")
    
    if os.path.exists(dashboard_path):
        with open(dashboard_path, 'r') as f:
            content = f.read()
            
        if "Digital Notice Board" not in content:
            # Inject notice board into sidebarItems
            # assuming sidebarItems = [
            
            replacement = f"    const sidebarItems = [\n{notice_board_string.format(ws_path=ws_path)}"
            if "const sidebarItems = [" in content:
                content = content.replace("const sidebarItems = [", replacement, 1)
            elif "const sidebarItems = [\n" in content:
                content = content.replace("const sidebarItems = [\n", replacement, 1)

            with open(dashboard_path, 'w') as f:
                f.write(content)
                
        # Now extract the updated sidebar items content to put into NoticeBoard.tsx
        # Find everything between "const sidebarItems = [" and "];"
        
        start_idx = content.find("const sidebarItems = [\n")
        if start_idx == -1:
            start_idx = content.find("const sidebarItems = [")
            
        if start_idx != -1:
            start_idx = content.find("[", start_idx) + 1
            end_idx = content.find("];", start_idx)
            
            sidebar_content = content[start_idx:end_idx]
            
            nb_code = notice_board_component.replace("{sidebar_items_content}", sidebar_content)
            
            with open(notice_board_path, 'w') as f:
                f.write(nb_code)

print("Updated Dashboards and created NoticeBoards.")
