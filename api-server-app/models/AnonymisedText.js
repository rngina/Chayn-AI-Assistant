module.exports = (sequelize, DataTypes) => {
    const AnonymizedText = sequelize.define('AnonymizedText', {
        text: {
            type: DataTypes.TEXT,
            allowNull: false,
        },
        createdAt: {
            type: DataTypes.DATE,
            defaultValue: DataTypes.NOW,
        },
    });
    return AnonymizedText;
};
