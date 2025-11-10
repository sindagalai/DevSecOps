export default [
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
    },
    rules: {
      "no-eval": "error",
      "no-unused-vars": "warn",
      "no-alert": "warn"
    }
  }
];
