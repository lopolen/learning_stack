(column_name | type | nullable / not null, unique, PK etc | explaination)

| id            | int       | PK, auto increment        | unique user id
| email         | varchar   | unique, not null          | user's email that will be used for login. Should be unique, and also normilized
| password_hash | varchar   | not null                  | user's password hash. Should never store password as a plain text
| is_active     | bool      | not null                  | account status, wich displays if its active. Can be used to ban users etc
| created_at    | timestamp | not null, default=now()   | Displays when user was created for logging reason.
