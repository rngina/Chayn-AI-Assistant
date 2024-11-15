const Sequelize = require('sequelize');
const sequelize = require('../config/db');

const AnonymizedText = require('./AnonymizedText')(sequelize, Sequelize.DataTypes);
const Letter = require('./Letter')(sequelize, Sequelize.DataTypes);

sequelize.sync({ alter: true })
    .then(() => console.log('Database & tables created!'))
    .catch((error) => console.error('Error creating database tables:', error));

module.exports = { sequelize, AnonymizedText, Letter };
