<script>
import UploadForm from './../components/UploadForm.vue'
    export default {
        data() {
            return {};
        },
        components: { UploadForm }
    };
</script>

<template>
    <div class="form-container">
        <h2>Upload Form</h2>
        <UploadForm />
    </div>
</template>

<style>
h2 {
    display: flex;
    justify-content: center;
}
</style> 