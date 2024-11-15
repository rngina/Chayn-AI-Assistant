const sequelize = require('../config/db');

(async () => {
    try {
        await sequelize.authenticate();
        console.log('Database connection successful!');
    } catch (error) {
        console.error('Database connection failed:', error.message);
    } finally {
        await sequelize.close(); // Close the connection after testing
    }
})();
