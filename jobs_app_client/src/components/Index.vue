
<template>
  <div>
    <p class="display-4">Job Openings</p>

    <div v-for="item in items" :key="item.id">
      <div class="card" style="width: ">
        <div class="card-body">
          <h5 class="card-title">{{ item.job_title }}</h5>
          <h6 class="card-subtitle mb-2 text-muted">
            {{ item.job_requirements }}
          </h6>
          <p class="card-subtitle mb-2 text-muted">
            {{ item.job_Description }}
          </p>
          <p class="card-text">Location: {{ item.job_location }}</p>
          <p class="card-text">salary: {{ item.job_salary }}</p>
          <p class="card-text">timing: {{ item.job_timings }}</p>
          <div v-if="item.applied === false">
            <p class="btn btn-success">Job Status: Still Open</p>
          </div>
          <div v-else-if="item.applied === true">
            <p class="btn btn-danger">Job Closed</p>
          </div>
          <div style="float: right">
            <router-link
              :to="{ name: 'Edit', params: { id: item.id } }"
              class="btn btn-primary"
              >edit</router-link
            >
            <router-link
              :to="{ name: 'Apply', params: { id: item.title } }"
              class="btn btn-primary"
              >Apply</router-link
            >
            <button class="btn btn-danger" v-on:click="deleteItem(item.id)">
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
    };
  },
  created: function () {
    this.fetchItems();
  },
  methods: {
    fetchItems() {
      let uri = "http://localhost:8000/jobs";
      this.axios.get(uri).then((response) => {
        this.items = response.data;
      });
    },
    deleteItem(id) {
      let uri = "http://localhost:8000/jobs/delete/" + id;
      this.items.splice(id, -1);
      this.axios.delete(uri);
    },
  },
};
</script>