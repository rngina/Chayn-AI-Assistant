module.exports = (sequelize, DataTypes) => {
    const Letter = sequelize.define('Letter', {
        content: {
            type: DataTypes.TEXT,
            allowNull: false,
        },
        createdAt: {
            type: DataTypes.DATE,
            defaultValue: DataTypes.NOW,
        },
    });
    return Letter;
};
