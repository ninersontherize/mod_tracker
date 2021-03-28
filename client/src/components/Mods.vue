<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Modifications</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.mod-modal>Add Mod</button>
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
    <b-modal ref="addModModal" id="mod-modal" title="Add a New mod" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-section-group"
                      label="Section:"
                      label-for="form-section-input">
          <b-form-input id="form-section-input"
                        type="text"
                        v-model="addModForm.section"
                        required
                        placeholder="Enter Section (Wheels, Body, Exhaust etc)">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-part-group"
                      label="Part Name:"
                      label-for="form-part-input">
          <b-form-input id="form-part-input"
                        type="text"
                        v-model="addModForm.part_name"
                        required
                        placeholder="Enter Part Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-link-group"
                      label="Link:"
                      label-for="form-link-input">
          <b-form-input id="form-link-input"
                        type="text"
                        v-model="addModForm.link"
                        required
                        placeholder="Paste Link Here">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-price-group"
                      label="Price:"
                      label-for="form-price-input">
          <b-form-input id="form-price-input"
                        type="text"
                        v-model="addModForm.price"
                        required
                        placeholder="Paste Price Here">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-purchased-group">
          <b-form-checkbox-group v-model="addModForm.purchased" id="form-checks">
            <b-form-checkbox value="true">Purchased?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-form-group id="form-installed-group">
          <b-form-checkbox-group v-model="addModForm.installed" id="form-checks">
            <b-form-checkbox value="true">Installed?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset Form</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      mods: [],
      addModForm: {
        section: '',
        part_name: '',
        link: '',
        price: '',
        purchased: [],
        installed: [],
      },
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
    addMod(payload) {
      const path = 'http://localhost:5000/mods';
      axios.post(path, payload)
        .then(() => {
          this.getMods();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMods();
        });
    },
    initForm() {
      this.addModForm.section = '';
      this.addModForm.part_name = '';
      this.addModForm.link = '';
      this.addModForm.price = '';
      this.addModForm.purchased = [];
      this.addModForm.installed = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addModModal.hide();
      let purchased = false;
      let installed = false;
      if (this.addModForm.purchased[0]) purchased = true;
      if (this.addModForm.installed[0]) installed = true;
      const payload = {
        section: this.addModForm.section,
        part_name: this.addModForm.part_name,
        link: this.addModForm.link,
        price: this.addModForm.price,
        purchased,
        installed,
      };
      this.addMod(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addModModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getMods();
  },
};
</script>
