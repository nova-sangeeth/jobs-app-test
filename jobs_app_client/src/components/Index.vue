
<template>
  <div>
    <h1>Jobs Available.</h1>

    <table class="table table-hover">
      <thead>
        <tr>
          <td>JOB=ID</td>
          <td>title</td>
          <td>description</td>
          <td>requirements</td>
          <td>location</td>
          <td>timings</td>
          <td>salary</td>
        </tr>
      </thead>

      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.job_title }}</td>
          <td>{{ item.job_Description }}</td>
          <td>{{ item.job_requirements }}</td>
          <td>{{ item.job_location }}</td>
          <td>{{ item.job_timings }}</td>
          <td>{{ item.job_salary }}</td>
          <td>
            <router-link
              :to="{ name: 'Edit', params: { id: item.id } }"
              class="btn btn-primary"
              >Edit</router-link
            >
          </td>
          <td>
            <button class="btn btn-danger" v-on:click="deleteItem(item.id)">
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
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
    deleteItem(job_id) {
      let uri = "http://localhost:8000/jobs/" + job_id;
      this.items.splice(job_id, 1);
      this.axios.delete(uri);
      console.log(this.uri + job_id);
    },
  },
};
</script>