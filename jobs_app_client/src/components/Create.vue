<template>
  <div class="container">
        <div class="card">
            <div class="card-header">
                <h3>Post A Job....</h3>
            </div>
            <div class="card-body">
                <form v-on:submit.prevent="addItem">
                    <div class="form-group">
                        <label>Job ID</label>
                        <input type="text" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label>Job title:</label>
                        <input type="text" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label>Job desc:</label>
                        <input type="text" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label>Job requirements:</label>
                        <input type="text" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label>Job locations:</label>
                        <input type="text" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label>Job timings:</label>
                        <input type="text" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label>Job salary:</label>
                        <input type="text" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <input type="submit" class="btn btn-primary" value="Add job"/>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {

  data() {
      return {
          item: []
      }
  },
  methods: {
      addItem() {
           let uri = 'http://localhost:8000/jobs/add';
            this.axios.post(uri, this.item).then((response) => {
                console.log(response)
            });
        }
    }
}
</script>
