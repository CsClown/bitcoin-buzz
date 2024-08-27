const deleteButtons = document.getElementsByClassName("btn-delete");
const replyText = document.getElementById("id_body");
const replyForm = document.getElementById("replyForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes delete functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated reply's ID upon click.
* - Fetches the content of the corresponding reply.
* - Populates the `replyText` input/textarea with the reply's content for deleting.
* - dupdates the submit button's text to "delete".
* - Sets the form's action attribute to the `delete_reply/{replyId}` endpoint.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let replyId = e.target.getAttribute("reply_id");
    let replyContent = document.getElementById(`reply${replyId}`).innerText;
    replyText.value = replyContent;
    submitButton.innerText = "delete";
    replyForm.setAttribute("action", `delete_reply/${replyId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated reply's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific reply.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let replyId = e.target.getAttribute("reply_id");
      deleteConfirm.href = `delete_reply/${replyId}`;
      deleteModal.show();
    });
  }