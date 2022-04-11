<template>

<form @submit.prevent="uploadPhoto" id="uploadForm" method="POST" enctype="multipart/form-data">'

	<label class="label" for="description">Description</label>
    <input type="text" name="description" v-model="description" id="description" class="form-control" placeholder="Add Description"/>
	<label class="label" for="upload">Upload Photo</label>
    <input type="file" name="upload" id="upload" class="form-control" placeholder="Upload an Image"/>
	<button class="btn">Upload</button>

</form>

</template>

<script>
    export default {
        data() {
            return {
                csrf_token: '',
            }
        },
        methods: {
            uploadPhoto() {
                const self = this;
                let uploadForm = document.getElementById('uploadForm');
                let form_data = new FormData(uploadForm);
                fetch("/api/upload", {method: 'POST', body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                    }
                }).then(function (response) {
                    return response.json();
                }).then(function (data) {
                    // display a success message
                    console.log(data);
                }).catch(function (error) {
                    console.log(error);
                });
            },
            getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
            }
        },
        created() {
            this.getCsrfToken();
        }
    }
</script>

<style>

.btn {
   background-color: blue;
   color: #fff;
}
</style> 