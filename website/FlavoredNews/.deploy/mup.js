module.exports = {
  servers: {
    one: {
      host: '13.84.47.59',
      username: 'flavorednews',
      // pem:
      password:'Flavorednews16',
      // or leave blank for authenticate from ssh-agent
    }
  },

  meteor: {
    name: 'Flavored News',
    path: '../app',
    servers: {
      one: {}
    },
    buildOptions: {
      serverOnly: false,
    },
    env: {
      ROOT_URL: 'app.com',
      MONGO_URL: 'mongodb://localhost/meteor'
    },

    //dockerImage: 'kadirahq/meteord'
    deployCheckWaitTime: 60
  },

  mongo: {
    oplog: true,
    port: 27017,
    servers: {
      one: {},
    },
  },
};