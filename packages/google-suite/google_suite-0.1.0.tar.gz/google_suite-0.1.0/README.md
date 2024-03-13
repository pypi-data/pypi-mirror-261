# Google Suite

Automate handling of various Google Suite APIs such as Gmail, Blogger, etc.

## Setup

- `poetry install` if you want some helpful tools `poetry install --dev`
- `poetry shell` to enter the virtual environment
- Make sure you have your Google token and credentials for your project from Google Cloud. You can follow the steps [here](https://developers.google.com/gmail/api/quickstart/python) to get started.

## gmail.py

Quick overview of the methods:

| Name                 | Description                                                                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| list_labels          | List of labels (returns a dict)                                                                                                                                            |
| create_label         | Creates a label                                                                                                                                                            |
| update_label         | Updates a label                                                                                                                                                            |
| delete_label         | Deletes a label                                                                                                                                                            |
| label_by_id          | Gets a label by id                                                                                                                                                         |
| label_by_name        | Gets a label by name                                                                                                                                                       |
| mark_read            | Marks an eamil as read by id                                                                                                                                               |
| mark_all_read        | Marks all emails as read given a label or sender or both                                                                                                                   |
| mark_unread          | Marks an email as unread by id                                                                                                                                             |
| list_messages        | List of messages                                                                                                                                                           |
| send_message         | Sends a message that can have with or without an attachment. If provided a threadId it will also reply within the email thread chain.                                      |
| download_attachment  | Downloads an attachment and puts it in the attachments directory. Returns the path of the attachment. Also marks the email as read                                         |
| download_attachments | Download attachments from a list of messages using a ThreadPool and puts it in the attachments directory. Returns the path of the attachment. Also marks the email as read |
| list_filters         | List of filters                                                                                                                                                            |
| get_filter           | Get a filter by id                                                                                                                                                         |
| create_filter        | Creates a filter                                                                                                                                                           |
| update_filter        | Updates a filter                                                                                                                                                           |
| delete_filter        | Deletes a filter                                                                                                                                                           |

## blogger.py

The `blogger.py` file contains methods to interact with the Blogger API:

| Method               | Description                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| list_blogs           | Lists all blogs by the user.                                                                          |
| list_posts           | Lists all posts in a specific blog.                                                                   |
| get_post_content     | Retrieves the content of a specific post.                                                             |
| search_post          | Searches for posts based on a query.                                                                  |
| insert_post          | Inserts a new post in the blog.                                                                       |
| delete_post_by_id    | Deletes a post by its ID.                                                                             |
| delete_post_by_title | Deletes a post by its title.                                                                          |
| list_comments        | Lists comments for a specific post.                                                                   |
| get_comment_by_id    | Retrieves a comment by its ID.                                                                        |
| list_comments_by_blog| Lists comments for the entire blog.                                                                   |
| mark_as_spam         | Marks a comment as spam.                                                                              |
| mark_as_not_spam     | Marks a comment as not spam.                                                                          |

## Utilizing the Service Object

The `util.py` file builds the service object to interact with the Google APIs. Ensure that the project is set up in the Google Cloud Platform, and the necessary permissions and correct access to the scopes for the APIs are granted.
