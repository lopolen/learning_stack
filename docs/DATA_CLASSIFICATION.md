Email and password hash are auth-critical information.
Email is the only identifier for user for now.

Any other data such as firstname, lastname, birthday is optional, and 
are not used during auth.

PII is a data wich identifies a user. It can be user's email, birthday, 
first or last name, region etc. You sould not store this kind of information
without any valuable reason. And in case you are storing it, you should
provide users their europenian rights (sudh as "oh, delete my data please" or
"can I have a copy of information such you have about me" etc.).
And you should store this data only while its needed - not forever.

PII data should be stored seperately from auth information, so it will
be more easy to delete them on user's request.
On user delete request you should delete row from users auth and users PII table.

Auth-critical information is usually stored in users table.
High-end developers or administrator ONLY should have access to such data.
Auth-critical and PII data should be protected on service level, not onli UI
If some of this data is required for technical support for example, you 
should mask this data, so manager can see only a small bit of information.

You should not log passwords or hashes
