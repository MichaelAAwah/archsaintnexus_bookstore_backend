# **Endpoints**

## **List Books Endpoint**

- **HTTP Method:** `GET`
- **URL:** `/api/books/`
- **Response:** Returns a list of all books 

## **Create Book Endpoint**

- **HTTP Method:** `POST`
- **URL:** `/api/books/create/`
- **Required Data:**
  - Book name as `book_name`
  - Author as `author`
  - Price as `price`
  - Image as `image`
  - Release Date as `release_date`
  - Publication Date as `pub_date`
- **Response:** Returns a book data in json format with image_url.

## **Update Book Endpoint**

- **HTTP Method:** `PUT`
- **URL:** `/api/books/<id>/update/`
- **Required Data:**
  - Book name as `book_name`
  - Author as `author`
  - Price as `price`
  - Image as `image`
  - Release Date as `release_date`
  - Publication Date as `pub_date`
- **Response:** Returns a success message.

## **Partial Update Book Endpoint**

- **HTTP Method:** `PATCH`
- **URL:** `/api/books/<id>/update/`
- **Response:** Returns a success message.

## **Delete Book Endpoint**

- **HTTP Method:** `DELETE`
- **URL:** `/api/books/<id>/delete/`
- **Response:** Returns a success message.

## **List Blogs Endpoint**

- **HTTP Method:** `GET`
- **URL:** `/api/blogs/`
- **Response:** Returns a list of all blogs 

## **Create Blog Endpoint**

- **HTTP Method:** `POST`
- **URL:** `/api/blogs/create/`
- **Required Data:**
  - Title as `title`
  - Author as `author`
  - Content as `content`
  - Image as `image`
- **Response:** Returns a blog data in json format with image_url.

## **Update Blog Endpoint**

- **HTTP Method:** `PUT`
- **URL:** `/api/blogs/<id>/update/`
- **Required Data:**
  - Title as `title`
  - Author as `author`
  - Content as `content`
  - Image as `image`
- **Response:** Returns a success message.

## **Partial Update Blog Endpoint**

- **HTTP Method:** `PATCH`
- **URL:** `/api/blogs/<id>/update/`
- **Response:** Returns a success message.

## **Delete Blog Endpoint**

- **HTTP Method:** `DELETE`
- **URL:** `/api/blogs/<id>/delete/`
- **Response:** Returns a success message.