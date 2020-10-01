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
            <input
              type="text"
              class="form-control"
              v-model.number="item.job_salary"
            />
          </div>
          <!-- <div class="form-group">
            <label>availability:</label>
            <input type="text" class="form-control" v-model="item.applied" />
          </div> -->
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
        job_title: "",
        job_description: "",
        job_requirements: "",
        job_location: "",
        job_timings: "",
        job_salary: "",
      },

      name: "",
    };
  },
  created: function () {
    this.getItem();
  },
  methods: {
    // getItem() {
    //   let uri = "http://localhost:8000/jobs/" + this.$route.params.id;
    //   this.axios.get(uri).then((response) => {
    //     console.log(response.data);
    //     this.item = response.data;
    //   });
    // },
    getItem() {
      let uri = "http://localhost:8000/jobs/" + this.$route.params.id;
      this.axios.get(uri).then((response) => {
        let {
          job_title,
          job_description,
          job_requirements,
          job_location,
          job_timings,
          job_salary,
        } = response.data;
        this.item = {
          job_title,
          job_description,
          job_requirements,
          job_location,
          job_timings,
          job_salary,
        };
      });
    },
    updateItem() {
      let uri = "http://localhost:8000/jobs/update/" + this.$route.params.id;
      console.log(uri);
      this.axios.put(uri, this.item).then((response) => {
        console.log(uri);
        console.log(response);
        this.item = response.data();
        this.$router.push({ name: "Index" });
      });
    },
  },
};
</script>