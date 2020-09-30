<template>
  <div class="container">
    <div class="card">
      <div class="card-header">
        <h3>Update the Job posting</h3>
      </div>
      <div class="card-body">
        <form v-on:submit.prevent="updateItem">
          <div class="form-group">
            <label>Job title:</label>

            <input type="text" class="form-control" v-model="item.job_title" />
          </div>
          <div class="form-group">
            <label>Job desc:</label>
            <input
              type="text"
              class="form-control"
              v-model="item.job_description"
            />
          </div>
          <div class="form-group">
            <label>Job requirements:</label>
            <input
              type="text"
              class="form-control"
              v-model="item.job_requirements"
            />
          </div>
          <div class="form-group">
            <label>Job locations:</label>
            <input
              type="text"
              class="form-control"
              v-model="item.job_location"
            />
          </div>
          <div class="form-group">
            <label>Job timings:</label>
            <input
              type="text"
              class="form-control"
              v-model="item.job_timings"
            />
          </div>
          <div class="form-group">
            <label>Job salary:</label>
            <input type="text" class="form-control" v-model="item.job_salary" />
          </div>
          <div class="form-group">
            <!-- <input type="submit" class="btn btn-primary" value="Update Item"  /> -->
            <button v-on:click="updateItem">Update</button>
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
      item: {
        job_title: null,
        job_Description: null,
        job_requirements: null,
        job_location: null,
        job_timings: null,
        job_salary: null,
      },
      name: "",
    };
  },
  created: function () {
    this.getItem();
  },
  methods: {
    getItem() {
      let uri = "http://localhost:8000/jobs/" + this.$route.params.id;
      this.axios.get(uri).then((response) => {
        this.item = response.data;
      });
    },
    updateItem() {
      // let uri = "http://localhost:8000/jobs/" + this.$route.params.id;
      this.axios
        .update("http://localhost:8000/jobs/" + this.$route.params.id)
        .then(
          (response) => console.log(response),
          this.$router.push({ name: "Index" })
        );
    },
  },
};
</script>