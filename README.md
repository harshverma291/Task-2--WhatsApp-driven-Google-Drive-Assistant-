# Task-2--WhatsApp-driven-Google-Drive-Assistant-
Step 1- Set up WhatsApp Integration
Choose a WhatsApp API or wrapper library, such as n8n's WhatsApp connector or another service.
Ensure it captures messages sent by you with commands
Step 2- Connect to Google Drive
Set up OAuth2 authentication with Google Drive so the tool can access your Drive safely.
Give the integration permissions to read, write, delete, move, rename, and upload files.
Step 3- Implement Command Handlers
Write functions (or scripts) that:
Listen for your WhatsApp messages.
Parse the commands like LIST, DELETE, MOVE, SUMMARY, RENAME, and UPLOAD.
Execute the corresponding Google Drive actions.
Step 4- Add AI Summary
Use an AI service like GPT or Claude.
When a SUMMARY command is received, fetch the files' text content and send it to the AI to get a summary.
Send the summary back to you via WhatsApp
Step 5- Handle File Uploads
When you send a file with a message containing an upload command, automatically save the file to the correct folder and rename it as per the message.
Step 6- Test and Deploy
Could you test all commands from WhatsApp to make sure everything works as expected?
If using n8n, export your workflow as workflow.json.
Otherwise, prepare your scripts with a clear guide on how to run them.
