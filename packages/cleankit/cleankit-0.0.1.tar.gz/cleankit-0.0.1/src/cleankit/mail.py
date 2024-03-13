import extract_msg
import os
import base64
import mimetypes
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional,Union
from datetime import datetime
import extract_msg
from IPython.display import display, HTML
from pydantic import BaseModel, EmailStr
from pathlib import Path
import re
import base64
from IPython.display import display, HTML
def convert_filename_to_mimetype(filename: str) -> str:
    #Convert a file name to its corresponding MIME type.
    """Example
    print(convert('file.pdf'))  # Output: application/pdf
    print(convert('file.txt'))  # Output: text/plain
    print(convert('file.jpeg')) # Output: image/jpeg
    print(convert('file.x'))  # Output: application/octet-stream
    """

    # Guess the MIME type based on the extension
    mime_type, _ = mimetypes.guess_type(filename, strict=False)

    # Return the MIME type, or a default 'application/octet-stream' if not found
    return mime_type if mime_type is not None else 'application/octet-stream'



class Attachment(BaseModel):
    file_name: str
    file_type: str
    file_size: Optional[int]=None
    file_content: bytes
    file_mime_type: str

class Email(BaseModel):
    sender: Union[EmailStr,str]
    recipients_to: list[EmailStr]
    recipients_cc: list[EmailStr] = []
    recipients_bcc: list[EmailStr] = []
    subject: Optional[str]
    body_plain: Optional[str] = None
    body_html: str=""
    sent_date: datetime
    attachments: list[Attachment] = []
    message_id: str  # Unique identifier for the email
    thread_id: Optional[str]
    references: list[str] = []  # Message-ID values of related emails (for threading)
    in_reply_to: Optional[str] = None  # Message-ID of the email this is a response to
    
    def __str__(self):
        attachments_info = "Attachments:\n" + "\n".join(
            [f" - Name: {a.file_name}, Type: {a.file_type}" for a in self.attachments]
        ) if self.attachments else "No attachments."
        
        content = "Content not available."
        body_text = display_email_plain(self)
        content = f"Plain Text Content:\n{body_text}"
        
        return f"{attachments_info}\n\n{content}"

class Thread(BaseModel):
    emails: list[Email]
    thread_id: Optional[str] = None


def save_attachments(email: Email, file_name:str):
    # Create a directory for the email based on subject and sent date
    # Use a valid representation for the filesystem
    #folder_name = f"{email.subject}_{email.sent_date.strftime('%Y%m%d%H%M%S')}"
    #folder_name = "saved_emails/"+folder_name.replace("/", "_").replace("\\", "_").replace(":", "_")
    folder_name = Path('saved_emails') / file_name
    os.makedirs(folder_name, exist_ok=True)
    
    # Iterate through attachments and save each
    for attachment in email.attachments:
        attachment_path = os.path.join(folder_name, attachment.file_name)
        with open(attachment_path, "wb") as file:
            file.write(attachment.file_content)
    print(f"{len(email.attachments)} attachments have been saved in the folder: {folder_name}")
    

    
def parse_msg_file(file_path: str) -> Email:
    
    
    with extract_msg.Message(file_path) as msg:
        recipient_dict = dict(zip([recipient.name for recipient in msg.recipients],[recipient.email for recipient in msg.recipients]))
        sender = msg.sender
        recipients_to = list(recipient_dict.values())
        recipients_cc = msg.cc.split(';') if msg.cc else []
        recipients_bcc: list[str] = []  # .msg format may not contain BCC information
        subject = msg.subject
        body_plain = msg.body
        body_html = msg.htmlBody
        sent_date = msg.date
        message_id = msg.messageId.strip()
        in_reply_to = msg.headerDict.get("In_reply_to",None)
        thread_id = msg.headerDict.get('Thread-Index',None)
        references:list[str] = []  # This may need custom logic based on your .msg files

        attachments: list[Attachment] = []
        for attachment in msg.attachments:
            #try: 
            attachments.append(Attachment(
                file_name=attachment.longFilename or attachment.shortFilename,
                file_type=attachment.extension,
                file_size = len(attachment.data),
                file_content=attachment.data,
                file_mime_type=convert_filename_to_mimetype(attachment.longFilename or attachment.shortFilename)
            ))

        email = Email(
            sender=sender,
            recipients_to=recipients_to,
            recipients_cc=recipients_cc,
            recipients_bcc=recipients_bcc,
            subject=subject,
            body_plain=body_plain,
            body_html=body_html,
            sent_date=sent_date,
            attachments=attachments,
            message_id=message_id,
            in_reply_to=in_reply_to,
            thread_id=thread_id,
            references=references,
        )
    return(email) 


def display_email(email: Email):
    """
    Displays the email content in a Jupyter notebook, embedding images at their correct positions.
    
    Parameters:
    - email: An instance of the Email class containing the email details.
    
    Example usage:
    full_path = '/path/to/email/file.msg'
    email = parse_msg_file(full_path)
    display_email(email)
    """
    
    # Start with the original HTML body content
    html_content = email.body_html
    
    # Process and replace image placeholders with base64 encoded images
    for attachment in email.attachments:
        if 'image' in attachment.file_mime_type:
            # Encode the image content to base64
            base64_img = base64.b64encode(attachment.file_content).decode('utf-8')
            # Create the data URI for the image
            img_data_uri = f"data:{attachment.file_mime_type};base64,{base64_img}"
            # Replace the cid reference with the actual data URI
            html_content = re.sub(
                f"src=\"cid:{attachment.file_name}@[^\"']+\"",
                f"src=\"{img_data_uri}\"",
                html_content,
                flags=re.IGNORECASE
            )
    
    # Display the HTML in the notebook
    display(HTML(html_content))

    
def display_email_plain(email: Email):
    #Displays the email content as plain text.
    
    """Example:
    full_path = '/path/to/email/file.msg'
    email = parse_msg_file(full_path)
    display_email(email)
    """
    # Prepare the email details as Markdown for better formatting in Jupyter
    
    email_content = f"""Email Subject: {email.subject if email.subject else "No Subject"}\n\n""" +f"""From: {email.sender}\n\n"""+f"""To: {", ".join(email.recipients_to)}\n\n\n"""
    
    
    # Include CC recipients if any
    if email.recipients_cc:
        email_content += f'Cc: {", ".join(email.recipients_cc)}'
    
    # Add the plain text body, ensuring it's treated as preformatted text
    body = email.body_plain if email.body_plain else "No content available."
    email_content += f"\n\n----\n{body}\n----"
    return(email_content)

