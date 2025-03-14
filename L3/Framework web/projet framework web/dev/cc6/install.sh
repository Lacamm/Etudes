echo 'INSTALLATION DES PACKAGES'
sleep .25
echo '.'
sleep .25
echo '.'
sleep .25
echo '.'
symfony composer require cebe/markdown
symfony composer require orm-fixtures --dev
npm install bootstrap
npm install
npm run dev
symfony composer install
symfony console doctrine:database:create
symfony console doctrine:migrations:migrate
symfony console doctrine:fixtures:load
symfony console cache:clear
symfony server:start --no-tls --d

