const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated post's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific post.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let postId = e.target.getAttribute("post_id");
      deleteConfirm.href = `delete_post/${postId}`;
      deleteModal.show();
    });
  }
