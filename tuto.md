# 📝 Guide pour Modifier le Menu du Site Muse Bar

Bonjour ! Ce guide va t'expliquer comment modifier le menu de ton site web facilement, sans avoir besoin de savoir coder.

---

## 📍 Où se trouve le fichier à modifier ?

Le fichier à modifier s'appelle : **`js/config/menu-config.js`**

Tu peux l'ouvrir avec n'importe quel éditeur de texte (Bloc-notes, TextEdit, etc.)

---

## 🔧 Comment Modifier un Produit Existant ?

### Exemple : Modifier le prix d'une bière

Voici comment modifier le prix d'un produit. Regarde cet exemple :

**AVANT :**

```javascript
{
  name: "BLONDE DE SOIF",
  price: "3.50€ / 6€",
  description: "La Cardamine - 4,5% alc (25cl / 50cl).",
}
```

**APRÈS :** (si tu veux changer le prix en 4€ / 7€)

```javascript
{
  name: "BLONDE DE SOIF",
  price: "4€ / 7€",
  description: "La Cardamine - 4,5% alc (25cl / 50cl).",
}
```

### ⚠️ Règles IMPORTANTES à respecter :

1. **Ne supprime JAMAIS les guillemets** `"` autour du texte
2. **Ne supprime JAMAIS les virgules** `,` à la fin de chaque ligne
3. **Ne supprime JAMAIS les accolades** `{` et `}`
4. **Fais attention aux majuscules et minuscules**

---

## ➕ Comment Ajouter un Nouveau Produit ?

### Exemple : Ajouter une nouvelle bière

Trouve la section "Bières" dans le fichier et ajoute un nouvel item. Regarde où ajouter :

**AJOUTER ICI :**

```javascript
{
  name: "SOUR IPA",
  price: "4.50€ / 7.50€",
  description: "Les deux amants - 5,0% alc (25cl / 50cl).",
},
{  ← AJOUTE TON NOUVEAU PRODUIT ICI (avec une virgule avant)
  name: "TA BIÈRE NOUVELLE",
  price: "5€ / 9€",
  description: "Description de ta bière.",
},
```

### Étapes pour ajouter :

1. Trouve la catégorie où tu veux ajouter (Grignotages, Apéritifs, Bières, etc.)
2. Trouve le dernier produit de cette catégorie
3. Ajoute une virgule `,` après le dernier produit
4. Ajoute ton nouveau produit entre accolades `{}`
5. N'oublie pas la virgule `,` à la fin !

---

## ➖ Comment Supprimer un Produit ?

Pour supprimer un produit, il suffit de :

1. Trouver le produit dans le fichier
2. Supprimer TOUT le bloc (depuis `{` jusqu'à `},`)
3. Si c'était le dernier produit, supprimer aussi la virgule du produit précédent

**Exemple à SUPPRIMER complètement :**

```javascript
{
  name: "SAUCISSON",
  price: "5.50€",
  description: "Saucisson traditionnel.",
},  ← Supprime tout ce bloc (avec la virgule)
```

---

## 📝 Modifier le Nom d'une Catégorie

### Exemple : Changer "Grignotages" en "Petites Bouchées"

**AVANT :**

```javascript
{
  id: "grignotages",
  name: "Grignotages",
```

**APRÈS :**

```javascript
{
  id: "grignotages",
  name: "Petites Bouchées",
```

⚠️ **Attention :** Ne change JAMAIS le `id:` (reste en minuscules avec des traits d'union)

---

## 🍹 Cas Spécial : Les Cocktails avec Sous-catégories

Les cocktails ont deux sous-catégories : "Avec Alcool" et "Sans Alcool"

Pour ajouter/modifier dans cette section, cherche :

```javascript
subcategories: [
  {
    name: "Avec Alcool",
    items: [
      // ICI sont les cocktails avec alcool
    ],
  },
  {
    name: "Sans Alcool",
    items: [
      // ICI sont les cocktails sans alcool
    ],
  },
];
```

---

## ✅ Checklist avant de Sauvegarder

Avant de fermer le fichier, vérifie :

- [ ] Toutes les accolades `{` et `}` sont bien fermées
- [ ] Tous les guillemets `"` sont bien présents
- [ ] Toutes les virgules `,` sont bien là (sauf pour le dernier item d'une liste)
- [ ] Pas d'erreur de frappe dans les noms, prix ou descriptions

---

## 🚨 Que faire si ça ne fonctionne pas ?

Si après avoir modifié le fichier, le site ne fonctionne plus :

1. **Vérifie les guillemets** : chaque texte doit être entre `"` et `"`
2. **Vérifie les virgules** : chaque item doit avoir une virgule `,` à la fin (sauf le dernier)
3. **Vérifie les accolades** : chaque `{` doit avoir un `}` correspondant
4. **Vérifie l'orthographe** : pas de fautes dans les mots-clés comme `name:`, `price:`, `description:`

---

## 📞 Besoin d'Aide ?

Si tu as un problème, note :

- Quelle ligne tu as modifiée
- Ce que tu as essayé de faire
- Le message d'erreur si il y en a un

Et contacte la personne qui a développé le site !

---

## 📚 Exemple Complet : Modifier un Produit de A à Z

Voici un exemple complet pour modifier "TARTINE" :

**ÉTAPE 1** : Trouve le produit

```javascript
{
  name: "TARTINE",
  price: "10€",
  description: "Pain maison, pesto rouge maison, roquette, artichaut, noix, miel.",
},
```

**ÉTAPE 2** : Modifie ce que tu veux (par exemple le prix)

```javascript
{
  name: "TARTINE",
  price: "12€",
  description: "Pain maison, pesto rouge maison, roquette, artichaut, noix, miel.",
},
```

**ÉTAPE 3** : Sauvegarde le fichier

**ÉTAPE 4** : Rafraîchis la page du site (F5 ou Ctrl+R)

Et voilà ! Le prix est maintenant à 12€ sur le site ! 🎉

---

**Bon courage et n'hésite pas à tester sur une copie du fichier avant de faire les vraies modifications !**
