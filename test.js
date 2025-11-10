// test.js - Exemple de failles pour ESLint et Semgrep

// ❌ Mauvaise pratique : mot de passe codé en dur
var password = "sindagalai123";

// ❌ Mauvaise pratique : exécution dynamique (risque d'injection)
eval("console.log('Mot de passe:', password)");
//console.log("Mot de passe:", password);

// ❌ Exemple de secret codé en dur (pour test)
const GITHUB_TOKEN = "ghp_FAUXTOKEN1234567890test";

