module.exports = {
  servers: {
    one: {
      host: '13.84.47.59',
      username: 'flavoredadmin',
      // pem:
      password:'Flavoredadmin16'
      // or leave blank for authenticate from ssh-agent
    }
  },

  meteor: {
    name: 'FlavoredNews',
    path: '../',
    servers: {
      one: {}
    },
    buildOptions: {
      serverOnly: false,
    },
    env: {
      ROOT_URL: 'http://13.84.47.59',
      MONGO_URL: 'mongodb://newsmood:hLQp9PBtdRnJGmKI9FegaJJPLI9T3Yl8vGHrwcXzYLt41dUXYZTzsoA27NrH001CxZbgA0Aqjbio4liIVxKkIA==@newsmood.documents.azure.com:10250/?ssl=true'
    },
    docker: {
      image:'abernix/meteord:base'
    },

    //dockerImage: 'kadirahq/meteord'
    deployCheckWaitTime: 60
  },

  mongo: {
    oplog: true,
    port: 27017,
    servers: {
      one: {}
    },
  },
};
