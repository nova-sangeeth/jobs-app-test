<template>
  <div class="container">
    <div class="card">
      <div class="card-header">
        <h3>Post A Job....</h3>
      </div>
      <div class="card-body">
        <form v-on:submit.prevent="addItem">
          <label>Job title:</label>
          <input type="text" class="form-control" v-model="job_title" />

          <label>Job desc:</label>
          <input type="text" class="form-control" v-model="job_description" />

          <label>Job requirements:</label>
          <input type="text" class="form-control" v-model="job_requirements" />

          <label>Job locations:</label>
          <input type="text" class="form-control" v-model="job_locations" />

          <label>Job timings:</label>
          <input type="text" class="form-control" v-model="job_timings" />

          <label>Job salary:</label>
          <input type="text" class="form-control" v-model="job_salary" />

          <input type="submit" class="btn btn-primary" value="Add job" />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  //   components: {
  // name: "AddItem",
  //   },
  data() {
    return {
      item: {},
    };
  },
  methods: {
    addItem() {
      let uri = "http://localhost:8000/jobs/add";
      this.axios
        .post(uri, this.item)
        .then((response) => console.log(response.data));
    },
  },
};
</script>
