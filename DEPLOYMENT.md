# 🚀 Guide de Déploiement - Site Web Muse Bar

Ce guide complet vous accompagne dans le déploiement du site web Muse Bar sur Cloudflare Pages.

## Prérequis

- ✅ Compte Cloudflare (vous en avez déjà un)
- ✅ Compte GitHub avec le dépôt
- ✅ Nom de domaine personnalisé (optionnel, mais recommandé)

---

## Étape 1 : Configuration de Cloudflare Pages

### 1.1 Accéder à Cloudflare Pages

1. Connectez-vous à votre [Tableau de bord Cloudflare](https://dash.cloudflare.com/)
2. Dans la barre latérale gauche, cliquez sur **"Pages"**
3. Cliquez sur **"Create a project"** ou **"Connect to Git"**

### 1.2 Connecter votre dépôt GitHub

1. Sélectionnez **"GitHub"** comme fournisseur Git
2. Autorisez Cloudflare à accéder à votre compte GitHub (si ce n'est pas déjà fait)
3. Sélectionnez le dépôt : **`VergneElliot/MuseBar`**
4. Cliquez sur **"Begin setup"**

### 1.3 Configurer les paramètres de build

Comme il s'agit d'un site statique sans processus de build, utilisez ces paramètres :

- **Nom du projet** : `muse-bar` (ou votre nom préféré)
- **Branche de production** : `main`
- **Commande de build** : Laisser vide (ou utiliser : `echo "No build needed"`)
- **Répertoire de sortie de build** : `.` (répertoire actuel - la racine du dépôt)

**Important** : Le répertoire de sortie de build doit être `.` car `index.html` est à la racine du dépôt.

### 1.4 Variables d'environnement

Aucune variable d'environnement n'est nécessaire pour ce site statique. Cliquez sur **"Save and Deploy"**.

### 1.5 Attendre le déploiement

Cloudflare Pages va :
1. Cloner votre dépôt
2. Déployer le site (devrait prendre 1-2 minutes)
3. Vous fournir une URL de prévisualisation : `https://muse-bar.pages.dev` (ou similaire)

---

## Étape 2 : Configuration du domaine personnalisé

### 2.1 Configuration DNS - Mise à jour des nameservers (ÉTAPE REQUISE EN PREMIER)

**IMPORTANT :** Avant de connecter votre domaine à Cloudflare Pages, vous devez mettre à jour vos nameservers chez votre registrar de domaine.

#### Étape 1 : Trouver votre registrar

1. Allez sur : https://lookup.icann.org/
2. Entrez : `musebar.fr`
3. Cliquez sur "Lookup"
4. Cherchez "Registrar" - cela vous indique où vous avez acheté le domaine

**Registrars courants :**
- OVH (commun pour les domaines .fr)
- Gandi
- Namecheap
- GoDaddy
- Google Domains

#### Étape 2 : Mettre à jour les nameservers chez votre registrar

1. **Connectez-vous au tableau de bord de votre registrar**
2. **Trouvez les paramètres nameserver/DNS** pour `musebar.fr`
3. **Remplacez les nameservers** par ceux de Cloudflare :
   - `anirban.ns.cloudflare.com`
   - `dorthy.ns.cloudflare.com`
   - Supprimez tous les anciens nameservers
   - Enregistrez les modifications

4. **Désactivez DNSSEC** (si activé) chez votre registrar

5. **Attendez 5-30 minutes** pour la propagation des nameservers

6. **Vérifiez dans Cloudflare :** Le badge "Invalid nameservers" devrait changer en "Active"

#### Étape 3 : Connecter le domaine dans Cloudflare Pages (DNS automatique)

Une fois les nameservers mis à jour et que Cloudflare affiche "Active" :

1. Allez dans votre projet Pages → onglet **Custom domains**
2. Cliquez sur **"Set up a custom domain"**
3. Entrez : `musebar.fr`
4. Cloudflare Pages va **automatiquement** :
   - Créer tous les enregistrements DNS nécessaires (A, CNAME, etc.)
   - Provisionner le certificat SSL
   - Connecter votre site au domaine

**Vous n'avez pas besoin d'ajouter manuellement des enregistrements DNS !** Cloudflare Pages gère tout automatiquement une fois les nameservers mis à jour.

### 2.2 Configuration SSL/TLS

1. Allez dans **SSL/TLS** dans votre tableau de bord Cloudflare
2. Assurez-vous que le mode de chiffrement SSL/TLS est défini sur **"Full"** ou **"Full (strict)"**
3. Cloudflare Pages provisionne automatiquement les certificats SSL (peut prendre quelques minutes)

### 2.3 Vérifier le domaine

1. Attendez 5-10 minutes pour la propagation DNS
2. Visitez votre domaine personnalisé dans un navigateur
3. Vous devriez voir votre site web Muse Bar !

### 2.4 Questions fréquentes sur le DNS

**Q : Dois-je ajouter manuellement des enregistrements DNS ?**
**R :** Non ! Une fois les nameservers mis à jour et le domaine connecté dans Cloudflare Pages, tous les enregistrements DNS sont créés automatiquement.

**Q : Mon site web sera-t-il hors ligne pendant ce processus ?**
**R :** Généralement non, mais il peut y avoir un bref moment pendant la transition. Le changement est généralement transparent.

**Q : Combien de temps cela prend-il ?**
**R :** 
- Mise à jour des nameservers : 5-30 minutes (parfois jusqu'à 48 heures)
- Création des enregistrements DNS : Automatique, se produit immédiatement après la mise à jour des nameservers
- Certificat SSL : 5-10 minutes après la connexion du domaine

**Q : Puis-je utiliser à la fois www et non-www ?**
**R :** Oui ! Après avoir connecté `musebar.fr`, vous pouvez également ajouter `www.musebar.fr` dans la section des domaines personnalisés de Cloudflare Pages. Cloudflare créera automatiquement les enregistrements DNS pour les deux.

---

## Étape 3 : Tester le déploiement

### 3.1 Tests de fonctionnalité de base

Testez les éléments suivants sur votre site déployé :

- [ ] **La page d'accueil se charge correctement**
  - Visitez votre domaine et vérifiez que la page se charge

- [ ] **La navigation fonctionne**
  - Cliquez sur tous les liens de navigation
  - Vérifiez que le défilement fluide fonctionne

- [ ] **Le menu s'affiche correctement**
  - Vérifiez que tous les éléments du menu se chargent
  - Vérifiez que les onglets du menu changent correctement
  - Testez sur mobile et desktop

- [ ] **Les images se chargent**
  - Vérifiez que toutes les images du carrousel s'affichent
  - Vérifiez le logo et les autres images

- [ ] **Les ressources externes**
  - L'intégration Google Maps devrait fonctionner
  - Les Google Fonts devraient se charger
  - Les icônes Font Awesome devraient s'afficher

- [ ] **Le design responsive**
  - Testez sur mobile (utilisez les outils de développement du navigateur)
  - Testez sur tablette
  - Testez sur desktop

- [ ] **Les performances**
  - Vérifiez la vitesse de chargement de la page
  - Vérifiez que HTTPS fonctionne (icône de cadenas vert)

### 3.2 Tests de navigateur

Testez dans plusieurs navigateurs :
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari (si disponible)
- [ ] Navigateurs mobiles (iOS Safari, Chrome Mobile)

### 3.3 Problèmes courants et solutions

#### Problème : Les fragments HTML ne se chargent pas
**Solution** : Cela signifie généralement que le site n'est pas servi via HTTPS. Cloudflare Pages fournit automatiquement HTTPS, donc cela ne devrait pas arriver. Si c'est le cas, vérifiez vos paramètres SSL/TLS.

#### Problème : Les images ne s'affichent pas
**Solution** : 
- Vérifiez que les chemins des images sont corrects (les chemins relatifs devraient fonctionner)
- Vérifiez que les images sont commitées dans le dépôt
- Vérifiez la console du navigateur pour les erreurs 404

#### Problème : Le domaine personnalisé ne fonctionne pas
**Solution** :
- Attendez 24-48 heures pour la propagation DNS complète
- Vérifiez que les enregistrements DNS sont corrects
- Vérifiez que le certificat SSL est provisionné (peut prendre quelques minutes)

#### Problème : Le style semble cassé
**Solution** :
- Videz le cache du navigateur (Ctrl+Shift+R ou Cmd+Shift+R)
- Vérifiez que tous les fichiers CSS se chargent (outils de développement du navigateur → onglet Network)
- Vérifiez que les chemins de fichiers sont corrects

---

## Étape 4 : Déploiement continu (mises à jour automatiques)

Cloudflare Pages déploie automatiquement lorsque vous poussez vers votre branche `main` :

1. Faites des modifications à votre code
2. Committez et poussez vers GitHub :
   ```bash
   git add .
   git commit -m "Update menu items"
   git push origin main
   ```
3. Cloudflare Pages va automatiquement :
   - Détecter le push
   - Déployer la nouvelle version
   - Mettre à jour votre site en direct (généralement en 1-2 minutes)

### 4.1 Déploiements de prévisualisation

Cloudflare Pages crée également des déploiements de prévisualisation pour les pull requests :
- Chaque PR obtient sa propre URL de prévisualisation
- Parfait pour tester les modifications avant de merger
- Les URLs de prévisualisation sont générées automatiquement

---

## Étape 5 : Surveillance et analytiques (optionnel)

### 5.1 Analytiques Cloudflare

Cloudflare Pages fournit des analytiques de base :
- Vues de page
- Utilisation de la bande passante
- Analytiques des requêtes

Accès via : Votre projet Pages → onglet **"Analytics"**

### 5.2 Analytiques personnalisées

Vous pouvez ajouter Google Analytics ou d'autres outils de suivi :
1. Ajoutez le code de suivi à `index.html` dans la section `<head>`
2. Committez et poussez
3. Déploiement automatique

---

## Dépannage

### Problème : Cloudflare Pages déploie un ancien commit

Si Cloudflare Pages déploie un ancien commit au lieu du dernier, suivez ces étapes :

#### Solution 1 : Déclencher un redéploiement manuel (recommandé)

1. **Allez dans le tableau de bord Cloudflare Pages**
   - Visitez : https://dash.cloudflare.com/
   - Naviguez vers : Pages → Votre projet (`muse-bar`)

2. **Déclencher un nouveau déploiement**
   - Cliquez sur l'onglet **"Deployments"**
   - Cliquez sur **"Retry deployment"** sur le déploiement échoué, OU
   - Cliquez sur **"Create deployment"** → Sélectionnez la branche `main` → Cliquez sur **"Deploy"**

3. **Vérifier le dernier commit**
   - Le déploiement devrait maintenant utiliser le dernier commit
   - Vérifiez les logs de déploiement pour confirmer

#### Solution 2 : Vérifier la configuration de la branche

1. **Vérifier les paramètres de branche**
   - Allez dans : Pages → Votre projet → **Settings** → **Builds & deployments**
   - Assurez-vous que la **branche de production** est définie sur : `main`
   - Assurez-vous que **Auto-deploy** est activé

2. **Vérifier le déclencheur de déploiement**
   - Allez dans : Pages → Votre projet → **Deployments**
   - Cherchez le dernier déploiement
   - Vérifiez qu'il déploie depuis le bon commit

#### Solution 3 : Forcer un push (si nécessaire)

Si ce qui précède ne fonctionne pas, vous pouvez créer un petit changement pour déclencher un nouveau déploiement :

```bash
cd MuseBar
# Faire un petit changement (comme mettre à jour un commentaire)
echo "# Optimisé pour Cloudflare Pages" >> README.md
git add README.md
git commit -m "Déclencher un nouveau déploiement"
git push origin main
```

Cela déclenchera Cloudflare Pages pour déployer automatiquement le dernier code.

#### Solution 4 : Vérifier le dépôt GitHub

Vérifiez que les fichiers sont bien dans GitHub :
1. Visitez : https://github.com/VergneElliot/MuseBar
2. Vérifiez que les fichiers sont présents
3. Vérifiez que le dernier commit est le bon

#### Solution 5 : Vider le cache Cloudflare

Si les déploiements utilisent encore d'anciens fichiers :

1. Allez dans : Tableau de bord Cloudflare → Votre domaine → **Caching** → **Configuration**
2. Cliquez sur **"Purge Everything"** (si disponible)
3. Ou attendez 5-10 minutes pour que le cache se vide

### Commande de correction rapide

Si vous voulez déclencher rapidement un nouveau déploiement :

```bash
cd MuseBar
git commit --allow-empty -m "Déclencher le redéploiement de Cloudflare Pages"
git push origin main
```

Cela crée un commit vide qui déclenchera Cloudflare Pages pour déployer le dernier code.

### Vérification du statut actuel

Pour vérifier que votre dépôt est prêt :

```bash
cd MuseBar

# Vérifier le dernier commit
git log --oneline -1

# Vérifier les tailles des images
ls -lh images/cavepv.png images/carrousel/cave.png

# Vérifier que le remote est correct
git remote -v
# Devrait afficher : https://github.com/VergneElliot/MuseBar.git
```

### Si vous avez encore des problèmes

1. **Vérifier les logs Cloudflare Pages**
   - Allez dans : Pages → Votre projet → Deployments → Cliquez sur le déploiement → Voir les logs
   - Cherchez le hash du commit dans les logs

2. **Vérifier le webhook GitHub**
   - Cloudflare Pages utilise les webhooks GitHub pour le déploiement automatique
   - Vérifiez si les webhooks sont correctement configurés dans les paramètres du dépôt GitHub

3. **Contacter le support**
   - Si rien de ce qui précède ne fonctionne, il pourrait y avoir un problème de configuration Cloudflare Pages
   - Consultez la documentation Cloudflare Pages ou le support

---

## Checklist de déploiement

### Pré-déploiement

- [ ] Le dépôt est poussé vers GitHub
- [ ] Tous les fichiers sont commités (vérifier avec `git status`)
- [ ] `index.html` est à la racine du dépôt
- [ ] Tous les assets (CSS, JS, images) sont dans le dépôt
- [ ] Testé localement avec `npm start` (le site fonctionne sur http://localhost:8000)

### Étape 1 : Configuration Cloudflare Pages

- [ ] Connecté au tableau de bord Cloudflare
- [ ] Navigué vers la section Pages
- [ ] Cliqué sur "Create a project" / "Connect to Git"
- [ ] Connecté le compte GitHub
- [ ] Sélectionné le dépôt : `VergneElliot/MuseBar`
- [ ] Configuré les paramètres de build :
  - [ ] Nom du projet : `muse-bar` (ou votre choix)
  - [ ] Branche de production : `main`
  - [ ] Commande de build : (laisser vide)
  - [ ] Répertoire de sortie de build : `.` (point/répertoire actuel)
- [ ] Cliqué sur "Save and Deploy"
- [ ] Déploiement terminé avec succès
- [ ] URL de prévisualisation fonctionne : `https://muse-bar.pages.dev` (ou similaire)

### Étape 2 : Configuration du domaine personnalisé

- [ ] Avoir votre nom de domaine prêt (ex. : `musebar.fr`)
- [ ] Mis à jour les nameservers chez votre registrar
- [ ] Désactivé DNSSEC (si activé)
- [ ] Vérifié que Cloudflare affiche "Active" pour les nameservers
- [ ] Dans le projet Pages, allé dans l'onglet "Custom domains"
- [ ] Cliqué sur "Set up a custom domain"
- [ ] Entré le nom de domaine
- [ ] Certificat SSL/TLS provisionné (vérifier l'onglet SSL/TLS)
- [ ] Attendu 5-10 minutes pour la propagation DNS
- [ ] Testé le domaine personnalisé dans le navigateur
- [ ] HTTPS fonctionne (icône de cadenas vert)

### Étape 3 : Tests

#### Tests de fonctionnalité
- [ ] Page d'accueil se charge
- [ ] Navigation fonctionne
- [ ] Menu s'affiche correctement
- [ ] Toutes les images se chargent
- [ ] Intégration Google Maps fonctionne
- [ ] Les polices se chargent correctement
- [ ] Les icônes s'affichent
- [ ] Le défilement fluide fonctionne
- [ ] Les animations fonctionnent

#### Tests responsive
- [ ] Vue mobile (< 576px)
- [ ] Vue tablette (768px - 991px)
- [ ] Vue desktop (1200px+)

#### Tests de navigateur
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari (si disponible)
- [ ] Navigateur mobile

#### Tests de performance
- [ ] La page se charge rapidement
- [ ] Aucune erreur dans la console (F12 → Console)
- [ ] Aucune erreur 404 (F12 → onglet Network)
- [ ] HTTPS est actif

### Étape 4 : Post-déploiement

- [ ] Mis en favoris le tableau de bord Cloudflare Pages
- [ ] Vérifié que les déploiements automatiques fonctionnent (push vers GitHub)
- [ ] Documenté le domaine personnalisé pour référence future
- [ ] Partagé l'URL du site avec l'équipe/les parties prenantes

### Avant de mettre en ligne

Assurez-vous que :

- [ ] Le site se déploie avec succès sur Cloudflare Pages
- [ ] Le domaine personnalisé est configuré et fonctionne
- [ ] Le certificat SSL est actif (HTTPS fonctionne)
- [ ] Toutes les pages et sections se chargent correctement
- [ ] Les images et assets s'affichent correctement
- [ ] La navigation et les interactions fonctionnent
- [ ] Le site est responsive sur mobile/tablette/desktop
- [ ] Les performances sont acceptables
- [ ] Aucune erreur dans la console des outils de développement du navigateur

---

## Référence rapide

### Tableau de bord Cloudflare Pages
- **URL** : https://dash.cloudflare.com/
- **Section Pages** : Barre latérale gauche → "Pages"

### URLs de votre projet
- **URL de prévisualisation** : `https://muse-bar.pages.dev` (ou similaire)
- **Domaine personnalisé** : `https://yourdomain.com` (une fois configuré)

### Commandes utiles

```bash
# Tester localement avant de déployer
cd MuseBar
npm start
# Visitez http://localhost:8000

# Déployer (automatique via Git push)
git add .
git commit -m "Votre message de commit"
git push origin main
```

### Dépannage rapide

Si quelque chose ne fonctionne pas :

1. **Vérifier la console du navigateur** (F12 → Console) pour les erreurs
2. **Vérifier l'onglet Network** (F12 → Network) pour les requêtes échouées
3. **Vérifier le DNS** en utilisant `nslookup yourdomain.com` ou un vérificateur DNS en ligne
4. **Vérifier les logs Cloudflare Pages** dans le tableau de bord
5. **Vider le cache du navigateur** (Ctrl+Shift+R)
6. **Attendre la propagation DNS** (peut prendre jusqu'à 48 heures, généralement 5-10 minutes)

---

## Support et ressources

- **Documentation Cloudflare Pages** : https://developers.cloudflare.com/pages/
- **Support Cloudflare** : https://support.cloudflare.com/
- **Documentation DNS Cloudflare** : https://developers.cloudflare.com/dns/
- **Dépôt GitHub** : https://github.com/VergneElliot/MuseBar

---

**🎉 Félicitations ! Votre site web Muse Bar est maintenant en ligne !**

Pour les mises à jour, il suffit de pousser vers GitHub et Cloudflare Pages déploiera automatiquement.
