const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");
const editButtons = document.getElementsByClassName("btn-edit");
const replyText = document.getElementById("id_content");
const replyForm = document.getElementById("replyForm");
const submitButton = document.getElementById("submitButton");

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



/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated reply's ID upon click.
* - Fetches the content of the corresponding reply.
* - Populates the `replyText` input/textarea with the reply's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_reply/{replyId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    console.log('edit button clicked');
    let replyId = e.target.getAttribute("reply_id");
    let replyContent = document.getElementById(`reply${replyId}`).innerText;
    replyText.value = replyContent;
    submitButton.innerText = "Update";
    replyForm.setAttribute("action", `edit_reply/${replyId}`);
  });
}