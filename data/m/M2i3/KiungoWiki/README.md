== Bienvenue sur KiungoWiki

Un site pour mettre en évidence le rôle des créateurs et interprêtes dans les oeuvres audios ainsi que les liens entre ces oeuvres dans le temps et l'espace.

=== Comment nous y arrivont

- établir les relations entre les chansons (entre elles), les artistes, les versions de chansons, etc.
- tout ce qui pourrait se retrouver sur un CD.... (par extension, tout ce qui peut se retrouver sur un vinyl, cassette, MP3).
- oeuvres musicales
- disques de monologues
- pistes sonores de spectacles/comédies musicales
- valoriser les gens qui contribe à la BD (par points, écusson, etc.)

=== Ce que ce site n'est pas

- pas bibliothèque de MP3, le site contient le métadata et les relations mais pas pistes musicales en soit.
- répéter complètement ce que d'autres sites fournissent.


-- ----------------------------------------------------------
-- MDB Tools - A library for reading MS Access database files
-- Copyright (C) 2000-2011 Brian Bruns and others.
-- Files in libmdb are licensed under LGPL and the utilities under
-- the GPL, see COPYING.LIB and COPYING files respectively.
-- Check out http://mdbtools.sourceforge.net
-- ----------------------------------------------------------

-- That file uses encoding UTF-8

CREATE TABLE [Albums]
 (
	[RefAlbum]			Long Integer NOT NULL, 
	[TitreAlbum]			Text (200), 
	[RefArtiste]			Long Integer, 
	[RefCategorieMusicale]			Long Integer, 
	[NoAlbum]			Text (40), 
	[NbrePieces]			Integer, 
	[Ordre1Alpha]			Text (100), 
	[Annee]			Long Integer, 
	[Ordre2Num]			Integer, 
	[Remarques]			Memo/Hyperlink (255), 
	[RefFormat]			Long Integer, 
	[RefEtiquette]			Long Integer
);

CREATE TABLE [Artistes] ** DONE
 (
	[RefArtiste]			Long Integer, 
	[NomArtiste]			Text (100), 
	[PrenomArtiste]			Text (100), 
	[DateNaissance]			Text (20), 
	[LieuNaissance]			Text (100), 
	[DateDeces]			Text (20), 
	[LieuDécès]			Text (100), 
	[Remarques]			Memo/Hyperlink (255), 
	[Collectif]			Boolean NOT NULL
);

CREATE TABLE [Categories musicales]
 (
	[RefCategorieMusicale]			Long Integer, 
	[CategorieMusicale]			Text (100)
);

CREATE TABLE [Éditeurs] ** DONE
 (
	[RefEditeur]			Long Integer, 
	[NomEditeur]			Text (100)
);

CREATE TABLE [Éléments du Menu Général]
 (
	[SwitchboardID]			Long Integer, 
	[ItemNumber]			Integer, 
	[ItemText]			Text (510), 
	[Command]			Integer, 
	[Argument]			Text (100)
);

CREATE TABLE [Étiquettes] ** DONE
 (
	[RefEtiquette]			Long Integer, 
	[NomEtiquette]			Text (100)
);

CREATE TABLE [Formats]
 (
	[RefFormat]			Long Integer, 
	[NomFormat]			Text (100)
);

CREATE TABLE [Langues]
 (
	[RefLangue]			Long Integer, 
	[Langue]			Text (100)
);

CREATE TABLE [Lien Artiste Auteur-compositeur] ** DONE
 (
	[RefPiece]			Long Integer, 
	[RefArtiste]			Long Integer, 
	[RefRole]			Long Integer
);

CREATE TABLE [Lien Artiste Interprete] ** DONE
 (
	[RéfVersion]			Long Integer, 
	[RefArtiste]			Long Integer, 
	[RefRole]			Long Integer
);

CREATE TABLE [Lien Editeur Piece] ** DONE
 (
	[RefPiece]			Long Integer, 
	[RefEditeur]			Long Integer
);

CREATE TABLE [Lien Propriete]
 (
	[RefProprietaire]			Long Integer, 
	[RefAlbum]			Long Integer
);

CREATE TABLE [Pieces] ** DONE
 (
	[RefPiece]			Long Integer, 
	[Titre]			Text (200), 
	[Annee]			Integer, 
	[RefLangue]			Long Integer, 
	[TexteVerifie]			Boolean NOT NULL, 
	[CreditsVerifie]			Boolean NOT NULL, 
	[RefPieceOriginale]			Long Integer, 
	[Remarque]			Memo/Hyperlink (255), 
	[Texte]			Memo/Hyperlink (255)
);

CREATE TABLE [Rythmes] ** DONE
 (
	[RefRythme]			Long Integer, 
	[Rythme]			Text (20), 
	[Tri]			Long Integer
);

CREATE TABLE [Versions]
 (
	[RefVersion]			Long Integer, 
	[Annee]			Integer, 
	[Duree]			DateTime, 
	[RefCategorieMusicale]			Long Integer, 
	[Remarque]			Memo/Hyperlink (255), 
	[RefRythme]			Long Integer, 
	[RefPiece]			Long Integer
);

CREATE TABLE [Lien Album Version]
 (
	[RefVersion]			Long Integer, 
	[RefAlbum]			Long Integer, 
	[Disque]			Text (10), 
	[Cote]			Text (2), 
	[Plage]			Integer, 
	[Remarque]			Memo/Hyperlink (255)
);

CREATE TABLE [Proprietaires]
 (
	[RefProprietaire]			Long Integer, 
	[NomProprietaire]			Text (100), 
	[PrenomProprietaire]			Text (100)
);

CREATE TABLE [Roles] ** DONE
 (
	[RefRole]			Long Integer, 
	[Role]			Text (100)
);

