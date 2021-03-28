<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Modifications</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Mod</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Section of Car</th>
              <th scope="col">Part</th>
              <th scope="col">Buy Link</th>
              <th scope="col">Best Price</th>
              <th scope="col">Purchased?</th>
              <th scope="col">Installed?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(mod, index) in mods" :key="index">
              <td>{{ mod.section }}</td>
              <td>{{ mod.part_name }} </td>
              <td class="d-inline-block text-truncate" style="max-width: 150px;">
                <a v-bind:href="mod.link">{{ mod.link }}</a>
              </td>
              <td>{{ mod.price }}</td>
              <td>
                <span v-if="mod.purchased">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <span v-if="mod.installed">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      mods: [],
    };
  },
  methods: {
    getMods() {
      const path = 'http://localhost:5000/mods';
      axios.get(path)
        .then((res) => {
          this.mods = res.data.mods;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMods();
  },
};
</script>
