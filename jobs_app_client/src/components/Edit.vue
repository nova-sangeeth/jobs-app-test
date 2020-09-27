<template>
  <div class="container">
        <div class="card">
            <div class="card-header">
                <h3>Update the Job posting</h3>
            </div>
            <div class="card-body">
                <form v-on:submit.prevent="updateItem">
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
                        <input type="submit" class="btn btn-primary" value="Update Item"/>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
export default{
        data(){
            return{
                item:{}
            }
        },

        created: function(){
            this.getItem();
        },

        methods: {
            getItem()
            {
              let uri = 'http://localhost:8000/jobs/' + this.$route.params.id;
                this.axios.get(uri).then((response) => {
                    this.item = response.data;
                });
            },

            updateItem()
            {
              let uri = 'http://localhost:8000/jobs/update/' + this.$route.params.id;
                this.axios.post(uri, this.item).then((response) => {
                    this.item = response.data;
                  this.$router.push({name: 'Index'});
                });
            }
        }
    }
</script>