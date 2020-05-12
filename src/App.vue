<template>

  <div id="app" >

    <h1> Music genre classification </h1>
      <b-container fluid class="text-center">
          <b-row>
              <b-col><div v-if="show_instructions" class="info" style="display: inline-block"> To test the model, upload a .mp3 song in one of the following eight genres:
                  <ul>
                      <li>Rock</li>
                      <li>Instrumental</li>
                      <li>Folk</li>
                      <li>Pop</li>
                      <li>Experimental</li>
                      <li>International</li>
                      <li>Hiphop</li>
                      <li>Electronic</li>
                  </ul>
                  </div></b-col>
              <b-col>

                  <div    v-if="show_upload"  class="upload-btn-wrapper">

                      <input type="file" id="input" multiple @change="onFileChange" accept=".mp3"/>
                  </div>
                  <div v-if="show_table">
                      <b-row align-text="right">
                          <div class="table_m">
                              <table class="table">
                                  <thead>
                                  <tr>
                                      <th scope="col">№</th>
                                      <th scope="col">file name</th>
                                      <th scope="col">size</th>
                                      <th scope="col">delete</th>
                                  </tr>
                                  </thead>
                                  <tbody >
                                  <tr  v-for="(i, j) in files" :key="j" class="row_table">
                                      <th scope="row">{{j+1}}</th>
                                      <td>{{i.name}}</td>
                                      <td>{{(i.size / 1024).toFixed(2)}} kb</td>
                                      <td>
                                   <span @click="delete_item(j)">
                                       <img alt ='img' title="delete this item"  width="105px" style="cursor: pointer; border-radius: 13px" :src="require('./assets/delete.png')">
                                   </span>
                                      </td>
                                  </tr>
                                  </tbody>

                              </table>
                          </div>
                      </b-row>
                      <b-row align-h="end" id="send_button">
                          <b-col cols="8"> <h1>Send files</h1> <img style="border-radius: 5px; cursor: pointer; margin-bottom: 5px" title="send files" v-show="files.length !== 0" @click="send" width="110px" :src="require('./assets/send1.png')" alt="">
                          </b-col>
                          <b-form-file placeholder="Chose files" v-if="files.length === 0" v-model="files" accept="files/*" multiple></b-form-file>
                      </b-row>

                  </div>
              </b-col>

          </b-row>
      </b-container>
  </div>

</template>


import axios from 'axios'
import { bus } from '../main'
<script>
    import {AxiosInstance as axios} from "axios";

    export default {
        name: 'Upload',
        data(){
            return  {
                files: [],
                show_instructions: true,
                show_upload: true,
                show_table: false,
                models: []
            }
        },
        methods: {
            onFileChange(e) {

                this.files = Object.values(e.target.files);
                console.log(this.files)
                this.show_instructions= true,
                this.show_table= true,

                this.show_upload=false

            },
            delete_item(index) {
                console.log("Removing", index);
                this.files.splice(index, 1);
                if (this.files.length === 0) {
                    this.show_table = false;
                    this.show_upload = true
                    this.show_table_files = false;

                }

            },
            send: function () {
                if (this.files.length !== 0) {
                    this.preloader = true
                    this.files_length = this.files.length
                    let files_pack = new FormData()
                    for (let i = 0; i < this.files.length; i++) {
                        files_pack.append("file", this.files[i])
                    }
                    files_pack.append("file", files_pack)
                    files_pack.append("id_style", this.index)
                    let headers;
                    headers = {
                        headers: {
                            'Content-Type': 'multipart/form-data',
                            'Access-Control-Allow-Origin': "*"
                        }
                    };
                    axios.post(this.API + '/upload', files_pack, headers)
                        .then((response) => {
                            this.get_img_paths()
                            this.download_url = response.data.link
                            this.preloader = false
                        })
                        // eslint-disable-next-line no-unused-vars
                        .catch((error) => {
                            this.preloader = false
                        })
                }
            },

            get_img_paths() {

            }
        }
    }
</script>


<style>

  #app {
  font-family: Brush Script MT, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  font-size: 47px;
}
  .info {

      text-align: start;
      height: 58vh;
      border: 1px groove deepskyblue;
      margin-top: 10px;
      margin-bottom: 1px;
      margin-left: 10px;
      margin-right: -10px;
      padding-left: 30px;
      padding-right: 10px;
      padding-top: 20px;
      font-size: 34px
  }
  h1 {

      margin: 0;
      margin-left: 10px;
      margin-right: -20px;
      padding-left: 0px;
      text-align: end;
      display: inline-block;

  }
  .img_upload{
      margin: 15px;
      padding: 5px 15px 5px 15px;
      border: 1px solid black;
      border-radius: 5px;
      background-color: aqua;
      width: 100px;
      cursor: pointer;
      text-align: center;
  }
body {
  margin: 0;
  background: url("./assets/back11.jpg") no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
.table{

    margin-top: 1px;
    margin-bottom: 1px;
    margin-left: 0px;
    margin-right: 20px;
    padding-left: 40px;
}

  .table_m {
      background-color:rgba(114, 92, 243, 0.5); height: 60vh; width: 90vh;
      border: 1px ridge rebeccapurple;
      overflow: auto;
      border-collapse: collapse;
      font-size: 30px;


  }
  .table_m::-webkit-scrollbar-track {
      -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
      background-color: #555555;
  }
  .table_m::-webkit-scrollbar {
      width: 5px;
      background-color: #F5F5F5;
  }
  .table_m::-webkit-scrollbar-thumb {
      background-color: #000000;
      border: 0px solid #555555;
  }
</style>

