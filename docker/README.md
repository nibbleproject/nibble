# Running with Docker

Nibble is available as a Docker image from the public Docker registry as
`nibbleproject/nibble`.

## Environment

- `DATABASE_URL` - URL of the database endpoint. This can be given to use an
  external database, and will override all other database connection settings,
  i.e. the database host, port, name, user, and password.
  The URL follows the schema described in the
  [`dj-database-url` docs](https://github.com/kennethreitz/dj-database-url#url-schema).
- `DATABASE_NAME` - Name of the database used by the app. Defaults to
  `nibble`. Only required if linking to a database container.
- `DATABASE_USER` - Name of the database user used by the app.
  Defaults to `test`. Only required if linking to a database container.
- `DATABASE_PASSWORD` - Name of the database user used by the app.
  Only required if linking to a database container.

## Database

The Docker image supports either an external database, or a linked container
based on the official `postgres` image.

### External

To connect to an external database, use the `DATABASE_URL` environment
variable, following the schema described in the
[`dj-database-url` docs](https://github.com/kennethreitz/dj-database-url#url-schema).

```bash
$ docker run -d -e DATABASE_URL=postgres://user:pass@host:5432/dbname web
```

### Linked

Nibble supports linking to the official `postgres` Docker image, and will
automatically discover the address, port, root username, and root password
based on the linked container's environment. The container must be linked as
`postgres` to enable autodiscovery.

When linking to a database container, you *must* provide the
`DATABASE_PASSWORD` environemnt variable to initialize the database
user.

```bash
$ docker run -d --name postgres postgres
$ docker run -d --link postgres:postgres \
    -e DATABASE_PASSWORD=butt web
```

This will initialize a database with the name `nibble`, belonging to a user
named `test` with the password `butt`. The user and database names can be
changed with `DATABASE_USER` and `DATABASE_NAME`, respectively.
