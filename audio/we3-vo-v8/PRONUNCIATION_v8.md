# WE3 VO v8: pronunciation list (Sound designer, 15 Nov 2026)

Only names that James actually speaks in v8 are listed. Names that stay on screen only (Edirne, Yedikule, Kafes, Szigetvár, Kahlenberg, Tanzimat, Kayser-i Rum, Sokollu, Kara Mustafa, Mahmud, Abdul Hamid, Sèvres, Harun Osman) need no voice.

Approach: the script file stays word for word. make_vo_v8.py swaps in a respelling only where eleven_v4 is likely to guess wrong (Turkish letters, Hungarian spelling, short words it misreads). Common English forms are left alone, because hyphenated respellings make James sound choppy. Years are sent as words so they are read the way a narrator says them. words.json keeps the script's own spelling.

## Respelled at record time

| Script | How to say it | Sent to ElevenLabs | Why |
|---|---|---|---|
| Söğüt | SUH-yoot (Turkish ö and ü, silent ğ) | Suh-yoot | Turkish letters; an English guess is "sog-gut" |
| devşirme | dev-sheer-MEH | dev-sheer-meh | ş = sh |
| Mohács | MOH-hahch | Moh-hahch | Hungarian cs = ch; a guess is "mo-hacks" |
| Hürrem | HOO-rem | Hoo-rem | Turkish ü |
| Hagia Sophia | HAH-yah so-FEE-ah | Hah-yah Sofia | avoids "HAY-jee-a" |
| gazis | GAH-zeez | gah-zees | short word, could be read "gay-zis" |
| bey | BAY | bay | could be read "bee" |
| HMS | H-M-S | H-M-S | read letter by letter |
| years (1300 ... 1932) | thirteen hundred, fourteen fifty-three, fourteen-oh-two, eighteen-nineties ... | as words | avoids "one thousand four hundred..." |

## Left as written (standard English form; check by ear)

| Name | Expected |
|---|---|
| Osman | OZ-mun (English usage; Turkish os-MAHN) |
| Orhan | or-HAHN |
| Bursa | BOOR-sah |
| Murad | moo-RAHD |
| Bayezid | BAH-yeh-zeed |
| Timur | tee-MOOR |
| Mehmed | MEH-med |
| Orban | OR-bahn |
| Selim | seh-LEEM |
| Suleiman | SOO-lay-mahn |
| Mustafa Kemal | MOOS-tah-fah keh-MAHL |
| Kosovo, Gallipoli, Ankara, Salonica, Anatolia | standard English |
| Mecca, Medina, Sunni, caliph | MEK-uh, meh-DEE-nuh, SOO-nee, KAY-lif |
| Janissaries | JAN-ih-sair-eez |
| HMS Malaya | muh-LAY-uh |

If any of these come out wrong, only that line is re-recorded and spliced (credits are low).
