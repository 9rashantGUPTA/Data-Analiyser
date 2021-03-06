# Generated by Django 2.2.4 on 2020-07-01 12:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('language', models.CharField(max_length=220, null=True)),
                ('category', models.CharField(choices=[('aml', 'aml'), ('analytics', 'analytics'), ('app', 'app'), ('assetmanagement', 'assetmanagement'), ('authentication', 'authentication'), ('blockchainexplorer', 'blockchainexplorer'), ('Blockchains', 'Blockchains'), ('blog', 'blog'), ('card', 'card'), ('community', 'community'), ('conference', 'conference'), ('consulting', 'consulting'), ('cryptobanking', 'cryptobanking'), ('cryptobrokerage', 'cryptobrokerage'), ('cryptoconglomerate', 'cryptoconglomerate'), ('cryptofinance', 'cryptofinance'), ('cryptofundofunds', 'cryptofundofunds'), ('cryptohedgefund', 'cryptohedgefund'), ('custody', 'custody'), ('dapp', 'dapp'), ('defi', 'defi'), ('derivatives', 'derivatives'), ('dex', 'dex'), ('ecommercetools', 'ecommercetools'), ('education', 'education'), ('exchange', 'exchange'), ('fintech', 'fintech'), ('gaming', 'gaming'), ('hardwarewallet', 'hardwarewallet'), ('informationhub', 'informationhub'), ('infrastructure', 'infrastructure'), ('investmentplatform', 'investmentplatform'), ('jobsincrypto', 'jobsincrypto'), ('kyc', 'kyc'), ('legal', 'legal'), ('lending', 'lending'), ('marketdata', 'marketdata'), ('marketingagency', 'marketingagency'), ('marketmaking', 'marketmaking'), ('marketplace', 'marketplace'), ('masternodes', 'masternodes'), ('medianetwork', 'medianetwork'), ('mining', 'mining'), ('newsletter', 'newsletter'), ('newsoutlet', 'newsoutlet'), ('nft', 'nft'), ('otc', 'otc'), ('payments', 'payments'), ('podcast', 'podcast'), ('portfoliotracker', 'portfoliotracker'), ('prfirm', 'prfirm'), ('protocol', 'protocol'), ('quantitativetrading', 'quantitativetrading'), ('research', 'research'), ('saas', 'saas'), ('shop', 'shop'), ('socialtrading', 'socialtrading'), ('staking', 'staking'), ('thinktank', 'thinktank'), ('tokensaleplatform', 'tokensaleplatform'), ('tokensolutions', 'tokensolutions'), ('tool', 'tool'), ('trading', 'trading'), ('tradingdesk', 'tradingdesk'), ('tradinggroup', 'tradinggroup'), ('venturecapital', 'venturecapital'), ('wallet', 'wallet'), ('wallet', 'wallet')], max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_name', models.CharField(max_length=220)),
                ('monthly_active_user', models.PositiveIntegerField()),
                ('global_rank', models.PositiveIntegerField()),
                ('country_traffic', models.CharField(max_length=220)),
                ('social_media_traffic', models.PositiveIntegerField()),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Brand')),
            ],
        ),
    ]
