# alu-back-end

Back-end projects and API exercises.

## Directories

### [api](./api)

REST API practice scripts.

| File | Description |
| --- | --- |
| [0-gather_data_from_an_API.py](./api/0-gather_data_from_an_API.py) | Given an employee ID, fetches the employee's TODO list from the JSONPlaceholder API using `requests` and displays their progress. |

#### Usage

```bash
./0-gather_data_from_an_API.py <employee_id>
```

Example:

```bash
$ python3 api/0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 voluptas quo tenetur perspiciatis explicabo natus
	 ...
```

Requirements:

- Python 3
- `requests` (`pip install requests`)
