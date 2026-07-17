# API Testing Assignment

## Objective

Automated API tests for

https://jsonplaceholder.typicode.com/posts

using Python and pytest.

---

## Project Structure

```
api-testing-assignment/
│
├── tests/
├── utils/
├── requirements.txt
├── pytest.ini
└── README.md
```

---

Create virtual environment

```
python -m venv venv
```

Activate


```

Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run tests

```bash
pytest
```

---

## Test Coverage

Positive Tests

- Get all posts
- Validate status code
- Validate response size
- Get single post

Negative Test

- Invalid post returns 404
