const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific item
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
// for (let button of deleteButtons) {
//     button.addEventListener("click", (e) => {
//       let replyId = e.target.getAttribute("reply_id");
//       deleteConfirm.href = `delete_reply/${replyId}`;
//       deleteModal.show();
//     });
//   }


  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let replyId = e.target.getAttribute("reply_id");
        let postId = e.target.getAttribute("post_id");

        if (replyId) {
            deleteConfirm.href = `delete_reply/${replyId}`;
        } else if (postId) {
            deleteConfirm.href = `delete_post/${postId}`;
        }

        deleteModal.show();
    });
}

// Toggle visibility of the reply form
document.getElementById("show-reply-form").addEventListener("click", function() {
    
    var replyFormContainer = document.getElementById("reply-form-container");
    if (replyFormContainer.style.display === "none") {
        replyFormContainer.style.display = "block";
        this.style.display = "none";  // Hide the "Reply to this Post" button
    }
});