const API = 'http://127.0.0.1:8000/api/books/';

const books = [];

const getBooks = async () => {
    await fetch(API)
    .then(response => response.json())
    .then(data => {
        books.push(...data);
    });
}

getBooks().then(() => {
   const bookList = document.getElementById('book-list');
   books.forEach(book => {
       const bookItem = document.createElement('div');
       bookItem.classList.add('book-item');
       bookItem.innerHTML = `
           <h2>${book.title}</h2>
           <p>Author: ${book.author}</p>
           <p>Published: ${book.published_date}</p>
           <img src="${book.cover}" alt="Cover image of ${book.title}" width="150" height="150" />
       `;
       bookList.appendChild(bookItem);
   });
});