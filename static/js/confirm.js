const deletes = document.getElementsByClassName("btn-delete");

const deletes_array = Array.from(deletes)
deletes_array.forEach((element) => {
  element.addEventListener("click", (e) => {
    if (!confirm("Are you sure of delete this conctact?")) {
      e.preventDefault();
    }
  });
});
