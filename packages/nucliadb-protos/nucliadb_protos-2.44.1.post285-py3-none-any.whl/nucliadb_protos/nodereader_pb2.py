# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/nodereader.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nucliadb_protos import noderesources_pb2 as nucliadb__protos_dot_noderesources__pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_noderesources__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_noderesources__pb2.nucliadb_protos.utils_pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from nucliadb_protos import utils_pb2 as nucliadb__protos_dot_utils__pb2

from nucliadb_protos.noderesources_pb2 import *
from nucliadb_protos.utils_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n nucliadb_protos/nodereader.proto\x12\nnodereader\x1a#nucliadb_protos/noderesources.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bnucliadb_protos/utils.proto\"L\n\x06\x46ilter\x12\x14\n\x0c\x66ield_labels\x18\x01 \x03(\t\x12\x18\n\x10paragraph_labels\x18\x02 \x03(\t\x12\x12\n\nexpression\x18\x03 \x01(\t\"\x82\x01\n\x0cStreamFilter\x12\x39\n\x0b\x63onjunction\x18\x01 \x01(\x0e\x32$.nodereader.StreamFilter.Conjunction\x12\x0e\n\x06labels\x18\x02 \x03(\t\"\'\n\x0b\x43onjunction\x12\x07\n\x03\x41ND\x10\x00\x12\x06\n\x02OR\x10\x01\x12\x07\n\x03NOT\x10\x02\"\x19\n\x07\x46\x61\x63\x65ted\x12\x0e\n\x06labels\x18\x01 \x03(\t\"\xc3\x01\n\x07OrderBy\x12\x11\n\x05\x66ield\x18\x01 \x01(\tB\x02\x18\x01\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x1d.nodereader.OrderBy.OrderType\x12/\n\x07sort_by\x18\x03 \x01(\x0e\x32\x1e.nodereader.OrderBy.OrderField\"\x1e\n\tOrderType\x12\x08\n\x04\x44\x45SC\x10\x00\x12\x07\n\x03\x41SC\x10\x01\"\'\n\nOrderField\x12\x0b\n\x07\x43REATED\x10\x00\x12\x0c\n\x08MODIFIED\x10\x01\"\xd2\x01\n\nTimestamps\x12\x31\n\rfrom_modified\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bto_modified\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x66rom_created\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nto_created\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\")\n\x0b\x46\x61\x63\x65tResult\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\r\n\x05total\x18\x02 \x01(\x05\"=\n\x0c\x46\x61\x63\x65tResults\x12-\n\x0c\x66\x61\x63\x65tresults\x18\x01 \x03(\x0b\x32\x17.nodereader.FacetResult\"\xc8\x03\n\x15\x44ocumentSearchRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x0e\n\x06\x66ields\x18\x03 \x03(\t\x12\"\n\x06\x66ilter\x18\x04 \x01(\x0b\x32\x12.nodereader.Filter\x12\"\n\x05order\x18\x05 \x01(\x0b\x32\x13.nodereader.OrderBy\x12$\n\x07\x66\x61\x63\x65ted\x18\x06 \x01(\x0b\x32\x13.nodereader.Faceted\x12\x13\n\x0bpage_number\x18\x07 \x01(\x05\x12\x17\n\x0fresult_per_page\x18\x08 \x01(\x05\x12*\n\ntimestamps\x18\t \x01(\x0b\x32\x16.nodereader.Timestamps\x12\x12\n\x06reload\x18\n \x01(\x08\x42\x02\x18\x01\x12\x14\n\x0conly_faceted\x18\x0f \x01(\x08\x12@\n\x0bwith_status\x18\x10 \x01(\x0e\x32&.noderesources.Resource.ResourceStatusH\x00\x88\x01\x01\x12\x1b\n\x0e\x61\x64vanced_query\x18\x11 \x01(\tH\x01\x88\x01\x01\x12\x11\n\tmin_score\x18\x12 \x01(\x02\x42\x0e\n\x0c_with_statusB\x11\n\x0f_advanced_query\"\xb3\x03\n\x16ParagraphSearchRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0e\n\x06\x66ields\x18\x03 \x03(\t\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x12\"\n\x06\x66ilter\x18\x05 \x01(\x0b\x32\x12.nodereader.Filter\x12\"\n\x05order\x18\x07 \x01(\x0b\x32\x13.nodereader.OrderBy\x12$\n\x07\x66\x61\x63\x65ted\x18\x08 \x01(\x0b\x32\x13.nodereader.Faceted\x12\x13\n\x0bpage_number\x18\n \x01(\x05\x12\x17\n\x0fresult_per_page\x18\x0b \x01(\x05\x12*\n\ntimestamps\x18\x0c \x01(\x0b\x32\x16.nodereader.Timestamps\x12\x12\n\x06reload\x18\r \x01(\x08\x42\x02\x18\x01\x12\x17\n\x0fwith_duplicates\x18\x0e \x01(\x08\x12\x14\n\x0conly_faceted\x18\x0f \x01(\x08\x12\x1b\n\x0e\x61\x64vanced_query\x18\x10 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x0bkey_filters\x18\x11 \x03(\t\x12\x11\n\tmin_score\x18\x12 \x01(\x02\x42\x11\n\x0f_advanced_query\",\n\x0bResultScore\x12\x0c\n\x04\x62m25\x18\x01 \x01(\x02\x12\x0f\n\x07\x62ooster\x18\x02 \x01(\x02\"e\n\x0e\x44ocumentResult\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12&\n\x05score\x18\x03 \x01(\x0b\x32\x17.nodereader.ResultScore\x12\r\n\x05\x66ield\x18\x04 \x01(\t\x12\x0e\n\x06labels\x18\x05 \x03(\t\"\xbb\x02\n\x16\x44ocumentSearchResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12+\n\x07results\x18\x02 \x03(\x0b\x32\x1a.nodereader.DocumentResult\x12>\n\x06\x66\x61\x63\x65ts\x18\x03 \x03(\x0b\x32..nodereader.DocumentSearchResponse.FacetsEntry\x12\x13\n\x0bpage_number\x18\x04 \x01(\x05\x12\x17\n\x0fresult_per_page\x18\x05 \x01(\x05\x12\r\n\x05query\x18\x06 \x01(\t\x12\x11\n\tnext_page\x18\x07 \x01(\x08\x12\x0c\n\x04\x62m25\x18\x08 \x01(\x08\x1aG\n\x0b\x46\x61\x63\x65tsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.nodereader.FacetResults:\x02\x38\x01\"\xf8\x01\n\x0fParagraphResult\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\r\n\x05\x66ield\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x04\x12\x11\n\tparagraph\x18\x06 \x01(\t\x12\r\n\x05split\x18\x07 \x01(\t\x12\r\n\x05index\x18\x08 \x01(\x04\x12&\n\x05score\x18\t \x01(\x0b\x32\x17.nodereader.ResultScore\x12\x0f\n\x07matches\x18\n \x03(\t\x12\x32\n\x08metadata\x18\x0b \x01(\x0b\x32 .noderesources.ParagraphMetadata\x12\x0e\n\x06labels\x18\x0c \x03(\t\"\xe8\x02\n\x17ParagraphSearchResponse\x12\x16\n\x0e\x66uzzy_distance\x18\n \x01(\x05\x12\r\n\x05total\x18\x01 \x01(\x05\x12,\n\x07results\x18\x02 \x03(\x0b\x32\x1b.nodereader.ParagraphResult\x12?\n\x06\x66\x61\x63\x65ts\x18\x03 \x03(\x0b\x32/.nodereader.ParagraphSearchResponse.FacetsEntry\x12\x13\n\x0bpage_number\x18\x04 \x01(\x05\x12\x17\n\x0fresult_per_page\x18\x05 \x01(\x05\x12\r\n\x05query\x18\x06 \x01(\t\x12\x11\n\tnext_page\x18\x07 \x01(\x08\x12\x0c\n\x04\x62m25\x18\x08 \x01(\x08\x12\x10\n\x08\x65matches\x18\t \x03(\t\x1aG\n\x0b\x46\x61\x63\x65tsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.nodereader.FacetResults:\x02\x38\x01\"\xf8\x01\n\x13VectorSearchRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06vector\x18\x02 \x03(\x02\x12\x14\n\x0c\x66ield_labels\x18\x03 \x03(\t\x12\x18\n\x10paragraph_labels\x18\x12 \x03(\t\x12\x13\n\x0bpage_number\x18\x04 \x01(\x05\x12\x17\n\x0fresult_per_page\x18\x05 \x01(\x05\x12\x12\n\x06reload\x18\r \x01(\x08\x42\x02\x18\x01\x12\x17\n\x0fwith_duplicates\x18\x0e \x01(\x08\x12\x12\n\nvector_set\x18\x0f \x01(\t\x12\x13\n\x0bkey_filters\x18\x10 \x03(\t\x12\x11\n\tmin_score\x18\x11 \x01(\x02\"&\n\x18\x44ocumentVectorIdentifier\x12\n\n\x02id\x18\x01 \x01(\t\"\x98\x01\n\x0e\x44ocumentScored\x12\x34\n\x06\x64oc_id\x18\x01 \x01(\x0b\x32$.nodereader.DocumentVectorIdentifier\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x31\n\x08metadata\x18\x03 \x01(\x0b\x32\x1f.noderesources.SentenceMetadata\x12\x0e\n\x06labels\x18\x04 \x03(\t\"s\n\x14VectorSearchResponse\x12-\n\tdocuments\x18\x01 \x03(\x0b\x32\x1a.nodereader.DocumentScored\x12\x13\n\x0bpage_number\x18\x04 \x01(\x05\x12\x17\n\x0fresult_per_page\x18\x05 \x01(\x05\"q\n\x12RelationNodeFilter\x12/\n\tnode_type\x18\x01 \x01(\x0e\x32\x1c.utils.RelationNode.NodeType\x12\x19\n\x0cnode_subtype\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0f\n\r_node_subtype\"\x95\x01\n\x12RelationEdgeFilter\x12\x33\n\rrelation_type\x18\x01 \x01(\x0e\x32\x1c.utils.Relation.RelationType\x12\x1d\n\x10relation_subtype\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x16\n\x0erelation_value\x18\x03 \x03(\tB\x13\n\x11_relation_subtype\"c\n\x1bRelationPrefixSearchRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x34\n\x0cnode_filters\x18\x02 \x03(\x0b\x32\x1e.nodereader.RelationNodeFilter\"B\n\x1cRelationPrefixSearchResponse\x12\"\n\x05nodes\x18\x01 \x03(\x0b\x32\x13.utils.RelationNode\"\x87\x02\n\x17\x45ntitiesSubgraphRequest\x12)\n\x0c\x65ntry_points\x18\x01 \x03(\x0b\x32\x13.utils.RelationNode\x12\x12\n\x05\x64\x65pth\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12M\n\x10\x64\x65leted_entities\x18\x04 \x03(\x0b\x32\x33.nodereader.EntitiesSubgraphRequest.DeletedEntities\x12\x16\n\x0e\x64\x65leted_groups\x18\x05 \x03(\t\x1a<\n\x0f\x44\x65letedEntities\x12\x14\n\x0cnode_subtype\x18\x01 \x01(\t\x12\x13\n\x0bnode_values\x18\x02 \x03(\tB\x08\n\x06_depth\">\n\x18\x45ntitiesSubgraphResponse\x12\"\n\trelations\x18\x01 \x03(\x0b\x32\x0f.utils.Relation\"\xad\x01\n\x15RelationSearchRequest\x12\x10\n\x08shard_id\x18\x01 \x01(\t\x12\x12\n\x06reload\x18\x05 \x01(\x08\x42\x02\x18\x01\x12\x37\n\x06prefix\x18\x0b \x01(\x0b\x32\'.nodereader.RelationPrefixSearchRequest\x12\x35\n\x08subgraph\x18\x0c \x01(\x0b\x32#.nodereader.EntitiesSubgraphRequest\"\x8a\x01\n\x16RelationSearchResponse\x12\x38\n\x06prefix\x18\x0b \x01(\x0b\x32(.nodereader.RelationPrefixSearchResponse\x12\x36\n\x08subgraph\x18\x0c \x01(\x0b\x32$.nodereader.EntitiesSubgraphResponse\"\xcb\x06\n\rSearchRequest\x12\r\n\x05shard\x18\x01 \x01(\t\x12\x0e\n\x06\x66ields\x18\x02 \x03(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\x12\"\n\x06\x66ilter\x18\x04 \x01(\x0b\x32\x12.nodereader.Filter\x12\"\n\x05order\x18\x05 \x01(\x0b\x32\x13.nodereader.OrderBy\x12$\n\x07\x66\x61\x63\x65ted\x18\x06 \x01(\x0b\x32\x13.nodereader.Faceted\x12\x13\n\x0bpage_number\x18\x07 \x01(\x05\x12\x17\n\x0fresult_per_page\x18\x08 \x01(\x05\x12*\n\ntimestamps\x18\t \x01(\x0b\x32\x16.nodereader.Timestamps\x12\x0e\n\x06vector\x18\n \x03(\x02\x12\x11\n\tvectorset\x18\x0f \x01(\t\x12\x12\n\x06reload\x18\x0b \x01(\x08\x42\x02\x18\x01\x12\x11\n\tparagraph\x18\x0c \x01(\x08\x12\x10\n\x08\x64ocument\x18\r \x01(\x08\x12\x17\n\x0fwith_duplicates\x18\x0e \x01(\x08\x12\x14\n\x0conly_faceted\x18\x10 \x01(\x08\x12\x1b\n\x0e\x61\x64vanced_query\x18\x12 \x01(\tH\x00\x88\x01\x01\x12@\n\x0bwith_status\x18\x11 \x01(\x0e\x32&.noderesources.Resource.ResourceStatusH\x01\x88\x01\x01\x12\x38\n\trelations\x18\x13 \x01(\x0b\x32!.nodereader.RelationSearchRequestB\x02\x18\x01\x12@\n\x0frelation_prefix\x18\x14 \x01(\x0b\x32\'.nodereader.RelationPrefixSearchRequest\x12>\n\x11relation_subgraph\x18\x15 \x01(\x0b\x32#.nodereader.EntitiesSubgraphRequest\x12\x13\n\x0bkey_filters\x18\x16 \x03(\t\x12\x1a\n\x12min_score_semantic\x18\x17 \x01(\x02\x12\x16\n\x0emin_score_bm25\x18\x19 \x01(\x02\x12&\n\x08security\x18\x18 \x01(\x0b\x32\x0f.utils.SecurityH\x02\x88\x01\x01\x42\x11\n\x0f_advanced_queryB\x0e\n\x0c_with_statusB\x0b\n\t_security\"\xbc\x01\n\x0eSuggestRequest\x12\r\n\x05shard\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12-\n\x08\x66\x65\x61tures\x18\x06 \x03(\x0e\x32\x1b.nodereader.SuggestFeatures\x12\"\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x12.nodereader.Filter\x12*\n\ntimestamps\x18\x04 \x01(\x0b\x32\x16.nodereader.Timestamps\x12\x0e\n\x06\x66ields\x18\x05 \x03(\t\"2\n\x0fRelatedEntities\x12\x10\n\x08\x65ntities\x18\x01 \x03(\t\x12\r\n\x05total\x18\x02 \x01(\r\"\xb1\x01\n\x0fSuggestResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12,\n\x07results\x18\x02 \x03(\x0b\x32\x1b.nodereader.ParagraphResult\x12\r\n\x05query\x18\x03 \x01(\t\x12\x10\n\x08\x65matches\x18\x04 \x03(\t\x12@\n\x0e\x65ntity_results\x18\x06 \x01(\x0b\x32(.nodereader.RelationPrefixSearchResponse\"\xe6\x01\n\x0eSearchResponse\x12\x34\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\".nodereader.DocumentSearchResponse\x12\x36\n\tparagraph\x18\x02 \x01(\x0b\x32#.nodereader.ParagraphSearchResponse\x12\x30\n\x06vector\x18\x03 \x01(\x0b\x32 .nodereader.VectorSearchResponse\x12\x34\n\x08relation\x18\x04 \x01(\x0b\x32\".nodereader.RelationSearchResponse\"\x1b\n\x0cIdCollection\x12\x0b\n\x03ids\x18\x01 \x03(\t\"Q\n\x0cRelationEdge\x12/\n\tedge_type\x18\x01 \x01(\x0e\x32\x1c.utils.Relation.RelationType\x12\x10\n\x08property\x18\x02 \x01(\t\"2\n\x08\x45\x64geList\x12&\n\x04list\x18\x01 \x03(\x0b\x32\x18.nodereader.RelationEdge\"_\n\x16RelationTypeListMember\x12/\n\twith_type\x18\x01 \x01(\x0e\x32\x1c.utils.RelationNode.NodeType\x12\x14\n\x0cwith_subtype\x18\x02 \x01(\t\"<\n\x08TypeList\x12\x30\n\x04list\x18\x01 \x03(\x0b\x32\".nodereader.RelationTypeListMember\"N\n\x0fGetShardRequest\x12(\n\x08shard_id\x18\x01 \x01(\x0b\x32\x16.noderesources.ShardId\x12\x11\n\tvectorset\x18\x02 \x01(\t\"+\n\rParagraphItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06labels\x18\x02 \x03(\t\";\n\x0c\x44ocumentItem\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12\x0e\n\x06labels\x18\x03 \x03(\t\"\xab\x01\n\rStreamRequest\x12\x32\n\x12\x66ilter__deprecated\x18\x01 \x01(\x0b\x32\x12.nodereader.FilterB\x02\x18\x01\x12\x12\n\x06reload\x18\x02 \x01(\x08\x42\x02\x18\x01\x12(\n\x08shard_id\x18\x03 \x01(\x0b\x32\x16.noderesources.ShardId\x12(\n\x06\x66ilter\x18\x04 \x01(\x0b\x32\x18.nodereader.StreamFilter\"(\n\x14GetShardFilesRequest\x12\x10\n\x08shard_id\x18\x01 \x01(\t\"5\n\rShardFileList\x12$\n\x05\x66iles\x18\x02 \x03(\x0b\x32\x15.nodereader.ShardFile\"0\n\tShardFile\x12\x15\n\rrelative_path\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x04\"C\n\x18\x44ownloadShardFileRequest\x12\x10\n\x08shard_id\x18\x01 \x01(\t\x12\x15\n\rrelative_path\x18\x02 \x01(\t\"-\n\x0eShardFileChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\r\n\x05index\x18\x02 \x01(\x05*/\n\x0fSuggestFeatures\x12\x0c\n\x08\x45NTITIES\x10\x00\x12\x0e\n\nPARAGRAPHS\x10\x01\x32\x85\n\n\nNodeReader\x12?\n\x08GetShard\x12\x1b.nodereader.GetShardRequest\x1a\x14.noderesources.Shard\"\x00\x12Y\n\x0e\x44ocumentSearch\x12!.nodereader.DocumentSearchRequest\x1a\".nodereader.DocumentSearchResponse\"\x00\x12\\\n\x0fParagraphSearch\x12\".nodereader.ParagraphSearchRequest\x1a#.nodereader.ParagraphSearchResponse\"\x00\x12S\n\x0cVectorSearch\x12\x1f.nodereader.VectorSearchRequest\x1a .nodereader.VectorSearchResponse\"\x00\x12Y\n\x0eRelationSearch\x12!.nodereader.RelationSearchRequest\x1a\".nodereader.RelationSearchResponse\"\x00\x12\x41\n\x0b\x44ocumentIds\x12\x16.noderesources.ShardId\x1a\x18.nodereader.IdCollection\"\x00\x12\x42\n\x0cParagraphIds\x12\x16.noderesources.ShardId\x1a\x18.nodereader.IdCollection\"\x00\x12?\n\tVectorIds\x12\x16.noderesources.ShardId\x1a\x18.nodereader.IdCollection\"\x00\x12\x41\n\x0bRelationIds\x12\x16.noderesources.ShardId\x1a\x18.nodereader.IdCollection\"\x00\x12?\n\rRelationEdges\x12\x16.noderesources.ShardId\x1a\x14.nodereader.EdgeList\"\x00\x12?\n\rRelationTypes\x12\x16.noderesources.ShardId\x1a\x14.nodereader.TypeList\"\x00\x12\x41\n\x06Search\x12\x19.nodereader.SearchRequest\x1a\x1a.nodereader.SearchResponse\"\x00\x12\x44\n\x07Suggest\x12\x1a.nodereader.SuggestRequest\x1a\x1b.nodereader.SuggestResponse\"\x00\x12\x46\n\nParagraphs\x12\x19.nodereader.StreamRequest\x1a\x19.nodereader.ParagraphItem\"\x00\x30\x01\x12\x44\n\tDocuments\x12\x19.nodereader.StreamRequest\x1a\x18.nodereader.DocumentItem\"\x00\x30\x01\x12N\n\rGetShardFiles\x12 .nodereader.GetShardFilesRequest\x1a\x19.nodereader.ShardFileList\"\x00\x12Y\n\x11\x44ownloadShardFile\x12$.nodereader.DownloadShardFileRequest\x1a\x1a.nodereader.ShardFileChunk\"\x00\x30\x01P\x00P\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nucliadb_protos.nodereader_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ORDERBY'].fields_by_name['field']._options = None
  _globals['_ORDERBY'].fields_by_name['field']._serialized_options = b'\030\001'
  _globals['_DOCUMENTSEARCHREQUEST'].fields_by_name['reload']._options = None
  _globals['_DOCUMENTSEARCHREQUEST'].fields_by_name['reload']._serialized_options = b'\030\001'
  _globals['_PARAGRAPHSEARCHREQUEST'].fields_by_name['reload']._options = None
  _globals['_PARAGRAPHSEARCHREQUEST'].fields_by_name['reload']._serialized_options = b'\030\001'
  _globals['_DOCUMENTSEARCHRESPONSE_FACETSENTRY']._options = None
  _globals['_DOCUMENTSEARCHRESPONSE_FACETSENTRY']._serialized_options = b'8\001'
  _globals['_PARAGRAPHSEARCHRESPONSE_FACETSENTRY']._options = None
  _globals['_PARAGRAPHSEARCHRESPONSE_FACETSENTRY']._serialized_options = b'8\001'
  _globals['_VECTORSEARCHREQUEST'].fields_by_name['reload']._options = None
  _globals['_VECTORSEARCHREQUEST'].fields_by_name['reload']._serialized_options = b'\030\001'
  _globals['_RELATIONSEARCHREQUEST'].fields_by_name['reload']._options = None
  _globals['_RELATIONSEARCHREQUEST'].fields_by_name['reload']._serialized_options = b'\030\001'
  _globals['_SEARCHREQUEST'].fields_by_name['reload']._options = None
  _globals['_SEARCHREQUEST'].fields_by_name['reload']._serialized_options = b'\030\001'
  _globals['_SEARCHREQUEST'].fields_by_name['relations']._options = None
  _globals['_SEARCHREQUEST'].fields_by_name['relations']._serialized_options = b'\030\001'
  _globals['_STREAMREQUEST'].fields_by_name['filter__deprecated']._options = None
  _globals['_STREAMREQUEST'].fields_by_name['filter__deprecated']._serialized_options = b'\030\001'
  _globals['_STREAMREQUEST'].fields_by_name['reload']._options = None
  _globals['_STREAMREQUEST'].fields_by_name['reload']._serialized_options = b'\030\001'
  _globals['_SUGGESTFEATURES']._serialized_start=6974
  _globals['_SUGGESTFEATURES']._serialized_end=7021
  _globals['_FILTER']._serialized_start=147
  _globals['_FILTER']._serialized_end=223
  _globals['_STREAMFILTER']._serialized_start=226
  _globals['_STREAMFILTER']._serialized_end=356
  _globals['_STREAMFILTER_CONJUNCTION']._serialized_start=317
  _globals['_STREAMFILTER_CONJUNCTION']._serialized_end=356
  _globals['_FACETED']._serialized_start=358
  _globals['_FACETED']._serialized_end=383
  _globals['_ORDERBY']._serialized_start=386
  _globals['_ORDERBY']._serialized_end=581
  _globals['_ORDERBY_ORDERTYPE']._serialized_start=510
  _globals['_ORDERBY_ORDERTYPE']._serialized_end=540
  _globals['_ORDERBY_ORDERFIELD']._serialized_start=542
  _globals['_ORDERBY_ORDERFIELD']._serialized_end=581
  _globals['_TIMESTAMPS']._serialized_start=584
  _globals['_TIMESTAMPS']._serialized_end=794
  _globals['_FACETRESULT']._serialized_start=796
  _globals['_FACETRESULT']._serialized_end=837
  _globals['_FACETRESULTS']._serialized_start=839
  _globals['_FACETRESULTS']._serialized_end=900
  _globals['_DOCUMENTSEARCHREQUEST']._serialized_start=903
  _globals['_DOCUMENTSEARCHREQUEST']._serialized_end=1359
  _globals['_PARAGRAPHSEARCHREQUEST']._serialized_start=1362
  _globals['_PARAGRAPHSEARCHREQUEST']._serialized_end=1797
  _globals['_RESULTSCORE']._serialized_start=1799
  _globals['_RESULTSCORE']._serialized_end=1843
  _globals['_DOCUMENTRESULT']._serialized_start=1845
  _globals['_DOCUMENTRESULT']._serialized_end=1946
  _globals['_DOCUMENTSEARCHRESPONSE']._serialized_start=1949
  _globals['_DOCUMENTSEARCHRESPONSE']._serialized_end=2264
  _globals['_DOCUMENTSEARCHRESPONSE_FACETSENTRY']._serialized_start=2193
  _globals['_DOCUMENTSEARCHRESPONSE_FACETSENTRY']._serialized_end=2264
  _globals['_PARAGRAPHRESULT']._serialized_start=2267
  _globals['_PARAGRAPHRESULT']._serialized_end=2515
  _globals['_PARAGRAPHSEARCHRESPONSE']._serialized_start=2518
  _globals['_PARAGRAPHSEARCHRESPONSE']._serialized_end=2878
  _globals['_PARAGRAPHSEARCHRESPONSE_FACETSENTRY']._serialized_start=2193
  _globals['_PARAGRAPHSEARCHRESPONSE_FACETSENTRY']._serialized_end=2264
  _globals['_VECTORSEARCHREQUEST']._serialized_start=2881
  _globals['_VECTORSEARCHREQUEST']._serialized_end=3129
  _globals['_DOCUMENTVECTORIDENTIFIER']._serialized_start=3131
  _globals['_DOCUMENTVECTORIDENTIFIER']._serialized_end=3169
  _globals['_DOCUMENTSCORED']._serialized_start=3172
  _globals['_DOCUMENTSCORED']._serialized_end=3324
  _globals['_VECTORSEARCHRESPONSE']._serialized_start=3326
  _globals['_VECTORSEARCHRESPONSE']._serialized_end=3441
  _globals['_RELATIONNODEFILTER']._serialized_start=3443
  _globals['_RELATIONNODEFILTER']._serialized_end=3556
  _globals['_RELATIONEDGEFILTER']._serialized_start=3559
  _globals['_RELATIONEDGEFILTER']._serialized_end=3708
  _globals['_RELATIONPREFIXSEARCHREQUEST']._serialized_start=3710
  _globals['_RELATIONPREFIXSEARCHREQUEST']._serialized_end=3809
  _globals['_RELATIONPREFIXSEARCHRESPONSE']._serialized_start=3811
  _globals['_RELATIONPREFIXSEARCHRESPONSE']._serialized_end=3877
  _globals['_ENTITIESSUBGRAPHREQUEST']._serialized_start=3880
  _globals['_ENTITIESSUBGRAPHREQUEST']._serialized_end=4143
  _globals['_ENTITIESSUBGRAPHREQUEST_DELETEDENTITIES']._serialized_start=4073
  _globals['_ENTITIESSUBGRAPHREQUEST_DELETEDENTITIES']._serialized_end=4133
  _globals['_ENTITIESSUBGRAPHRESPONSE']._serialized_start=4145
  _globals['_ENTITIESSUBGRAPHRESPONSE']._serialized_end=4207
  _globals['_RELATIONSEARCHREQUEST']._serialized_start=4210
  _globals['_RELATIONSEARCHREQUEST']._serialized_end=4383
  _globals['_RELATIONSEARCHRESPONSE']._serialized_start=4386
  _globals['_RELATIONSEARCHRESPONSE']._serialized_end=4524
  _globals['_SEARCHREQUEST']._serialized_start=4527
  _globals['_SEARCHREQUEST']._serialized_end=5370
  _globals['_SUGGESTREQUEST']._serialized_start=5373
  _globals['_SUGGESTREQUEST']._serialized_end=5561
  _globals['_RELATEDENTITIES']._serialized_start=5563
  _globals['_RELATEDENTITIES']._serialized_end=5613
  _globals['_SUGGESTRESPONSE']._serialized_start=5616
  _globals['_SUGGESTRESPONSE']._serialized_end=5793
  _globals['_SEARCHRESPONSE']._serialized_start=5796
  _globals['_SEARCHRESPONSE']._serialized_end=6026
  _globals['_IDCOLLECTION']._serialized_start=6028
  _globals['_IDCOLLECTION']._serialized_end=6055
  _globals['_RELATIONEDGE']._serialized_start=6057
  _globals['_RELATIONEDGE']._serialized_end=6138
  _globals['_EDGELIST']._serialized_start=6140
  _globals['_EDGELIST']._serialized_end=6190
  _globals['_RELATIONTYPELISTMEMBER']._serialized_start=6192
  _globals['_RELATIONTYPELISTMEMBER']._serialized_end=6287
  _globals['_TYPELIST']._serialized_start=6289
  _globals['_TYPELIST']._serialized_end=6349
  _globals['_GETSHARDREQUEST']._serialized_start=6351
  _globals['_GETSHARDREQUEST']._serialized_end=6429
  _globals['_PARAGRAPHITEM']._serialized_start=6431
  _globals['_PARAGRAPHITEM']._serialized_end=6474
  _globals['_DOCUMENTITEM']._serialized_start=6476
  _globals['_DOCUMENTITEM']._serialized_end=6535
  _globals['_STREAMREQUEST']._serialized_start=6538
  _globals['_STREAMREQUEST']._serialized_end=6709
  _globals['_GETSHARDFILESREQUEST']._serialized_start=6711
  _globals['_GETSHARDFILESREQUEST']._serialized_end=6751
  _globals['_SHARDFILELIST']._serialized_start=6753
  _globals['_SHARDFILELIST']._serialized_end=6806
  _globals['_SHARDFILE']._serialized_start=6808
  _globals['_SHARDFILE']._serialized_end=6856
  _globals['_DOWNLOADSHARDFILEREQUEST']._serialized_start=6858
  _globals['_DOWNLOADSHARDFILEREQUEST']._serialized_end=6925
  _globals['_SHARDFILECHUNK']._serialized_start=6927
  _globals['_SHARDFILECHUNK']._serialized_end=6972
  _globals['_NODEREADER']._serialized_start=7024
  _globals['_NODEREADER']._serialized_end=8309
# @@protoc_insertion_point(module_scope)
