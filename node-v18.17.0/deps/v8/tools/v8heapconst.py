#!/usr/bin/env python3
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
# yapf: disable

INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  96: "SHARED_STRING_TYPE",
  101: "SHARED_THIN_STRING_TYPE",
  104: "SHARED_ONE_BYTE_STRING_TYPE",
  109: "SHARED_THIN_ONE_BYTE_STRING_TYPE",
  128: "SYMBOL_TYPE",
  129: "BIG_INT_BASE_TYPE",
  130: "HEAP_NUMBER_TYPE",
  131: "ODDBALL_TYPE",
  132: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  133: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  134: "CALLABLE_TASK_TYPE",
  135: "CALLBACK_TASK_TYPE",
  136: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  137: "LOAD_HANDLER_TYPE",
  138: "STORE_HANDLER_TYPE",
  139: "FUNCTION_TEMPLATE_INFO_TYPE",
  140: "OBJECT_TEMPLATE_INFO_TYPE",
  141: "ACCESS_CHECK_INFO_TYPE",
  142: "ACCESSOR_INFO_TYPE",
  143: "ACCESSOR_PAIR_TYPE",
  144: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  145: "ALLOCATION_MEMENTO_TYPE",
  146: "ALLOCATION_SITE_TYPE",
  147: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  148: "ASM_WASM_DATA_TYPE",
  149: "ASYNC_GENERATOR_REQUEST_TYPE",
  150: "BREAK_POINT_TYPE",
  151: "BREAK_POINT_INFO_TYPE",
  152: "CACHED_TEMPLATE_OBJECT_TYPE",
  153: "CALL_HANDLER_INFO_TYPE",
  154: "CALL_SITE_INFO_TYPE",
  155: "CLASS_POSITIONS_TYPE",
  156: "DEBUG_INFO_TYPE",
  157: "ENUM_CACHE_TYPE",
  158: "ERROR_STACK_DATA_TYPE",
  159: "FEEDBACK_CELL_TYPE",
  160: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  161: "INTERCEPTOR_INFO_TYPE",
  162: "INTERPRETER_DATA_TYPE",
  163: "MODULE_REQUEST_TYPE",
  164: "PROMISE_CAPABILITY_TYPE",
  165: "PROMISE_ON_STACK_TYPE",
  166: "PROMISE_REACTION_TYPE",
  167: "PROPERTY_DESCRIPTOR_OBJECT_TYPE",
  168: "PROTOTYPE_INFO_TYPE",
  169: "REG_EXP_BOILERPLATE_DESCRIPTION_TYPE",
  170: "SCRIPT_TYPE",
  171: "SCRIPT_OR_MODULE_TYPE",
  172: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  173: "STACK_FRAME_INFO_TYPE",
  174: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  175: "TUPLE2_TYPE",
  176: "WASM_CONTINUATION_OBJECT_TYPE",
  177: "WASM_EXCEPTION_TAG_TYPE",
  178: "WASM_INDIRECT_FUNCTION_TABLE_TYPE",
  179: "FIXED_ARRAY_TYPE",
  180: "HASH_TABLE_TYPE",
  181: "EPHEMERON_HASH_TABLE_TYPE",
  182: "GLOBAL_DICTIONARY_TYPE",
  183: "NAME_DICTIONARY_TYPE",
  184: "NAME_TO_INDEX_HASH_TABLE_TYPE",
  185: "NUMBER_DICTIONARY_TYPE",
  186: "ORDERED_HASH_MAP_TYPE",
  187: "ORDERED_HASH_SET_TYPE",
  188: "ORDERED_NAME_DICTIONARY_TYPE",
  189: "REGISTERED_SYMBOL_TABLE_TYPE",
  190: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  191: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  192: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  193: "SCRIPT_CONTEXT_TABLE_TYPE",
  194: "BYTE_ARRAY_TYPE",
  195: "BYTECODE_ARRAY_TYPE",
  196: "FIXED_DOUBLE_ARRAY_TYPE",
  197: "INTERNAL_CLASS_WITH_SMI_ELEMENTS_TYPE",
  198: "SLOPPY_ARGUMENTS_ELEMENTS_TYPE",
  199: "TURBOFAN_BITSET_TYPE_TYPE",
  200: "TURBOFAN_HEAP_CONSTANT_TYPE_TYPE",
  201: "TURBOFAN_OTHER_NUMBER_CONSTANT_TYPE_TYPE",
  202: "TURBOFAN_RANGE_TYPE_TYPE",
  203: "TURBOFAN_UNION_TYPE_TYPE",
  204: "FOREIGN_TYPE",
  205: "WASM_INTERNAL_FUNCTION_TYPE",
  206: "WASM_TYPE_INFO_TYPE",
  207: "AWAIT_CONTEXT_TYPE",
  208: "BLOCK_CONTEXT_TYPE",
  209: "CATCH_CONTEXT_TYPE",
  210: "DEBUG_EVALUATE_CONTEXT_TYPE",
  211: "EVAL_CONTEXT_TYPE",
  212: "FUNCTION_CONTEXT_TYPE",
  213: "MODULE_CONTEXT_TYPE",
  214: "NATIVE_CONTEXT_TYPE",
  215: "SCRIPT_CONTEXT_TYPE",
  216: "WITH_CONTEXT_TYPE",
  217: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  218: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_AND_JOB_TYPE",
  219: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  220: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_WITH_JOB_TYPE",
  221: "WASM_FUNCTION_DATA_TYPE",
  222: "WASM_CAPI_FUNCTION_DATA_TYPE",
  223: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  224: "WASM_JS_FUNCTION_DATA_TYPE",
  225: "EXPORTED_SUB_CLASS_BASE_TYPE",
  226: "EXPORTED_SUB_CLASS_TYPE",
  227: "EXPORTED_SUB_CLASS2_TYPE",
  228: "SMALL_ORDERED_HASH_MAP_TYPE",
  229: "SMALL_ORDERED_HASH_SET_TYPE",
  230: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  231: "ABSTRACT_INTERNAL_CLASS_SUBCLASS1_TYPE",
  232: "ABSTRACT_INTERNAL_CLASS_SUBCLASS2_TYPE",
  233: "DESCRIPTOR_ARRAY_TYPE",
  234: "STRONG_DESCRIPTOR_ARRAY_TYPE",
  235: "SOURCE_TEXT_MODULE_TYPE",
  236: "SYNTHETIC_MODULE_TYPE",
  237: "WEAK_FIXED_ARRAY_TYPE",
  238: "TRANSITION_ARRAY_TYPE",
  239: "CELL_TYPE",
  240: "CODE_TYPE",
  241: "CODE_DATA_CONTAINER_TYPE",
  242: "COVERAGE_INFO_TYPE",
  243: "EMBEDDER_DATA_ARRAY_TYPE",
  244: "FEEDBACK_METADATA_TYPE",
  245: "FEEDBACK_VECTOR_TYPE",
  246: "FILLER_TYPE",
  247: "FREE_SPACE_TYPE",
  248: "INTERNAL_CLASS_TYPE",
  249: "INTERNAL_CLASS_WITH_STRUCT_ELEMENTS_TYPE",
  250: "MAP_TYPE",
  251: "MEGA_DOM_HANDLER_TYPE",
  252: "ON_HEAP_BASIC_BLOCK_PROFILER_DATA_TYPE",
  253: "PREPARSE_DATA_TYPE",
  254: "PROPERTY_ARRAY_TYPE",
  255: "PROPERTY_CELL_TYPE",
  256: "SCOPE_INFO_TYPE",
  257: "SHARED_FUNCTION_INFO_TYPE",
  258: "SMI_BOX_TYPE",
  259: "SMI_PAIR_TYPE",
  260: "SORT_STATE_TYPE",
  261: "SWISS_NAME_DICTIONARY_TYPE",
  262: "WASM_API_FUNCTION_REF_TYPE",
  263: "WASM_ON_FULFILLED_DATA_TYPE",
  264: "WEAK_ARRAY_LIST_TYPE",
  265: "WEAK_CELL_TYPE",
  266: "WASM_ARRAY_TYPE",
  267: "WASM_STRUCT_TYPE",
  268: "JS_PROXY_TYPE",
  1057: "JS_OBJECT_TYPE",
  269: "JS_GLOBAL_OBJECT_TYPE",
  270: "JS_GLOBAL_PROXY_TYPE",
  271: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1058: "JS_API_OBJECT_TYPE",
  2058: "JS_LAST_DUMMY_API_OBJECT_TYPE",
  2059: "JS_DATA_VIEW_TYPE",
  2060: "JS_TYPED_ARRAY_TYPE",
  2061: "JS_ARRAY_BUFFER_TYPE",
  2062: "JS_PROMISE_TYPE",
  2063: "JS_BOUND_FUNCTION_TYPE",
  2064: "JS_WRAPPED_FUNCTION_TYPE",
  2065: "JS_FUNCTION_TYPE",
  2066: "BIGINT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2067: "BIGUINT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2068: "FLOAT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2069: "FLOAT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2070: "INT16_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2071: "INT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2072: "INT8_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2073: "UINT16_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2074: "UINT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2075: "UINT8_CLAMPED_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2076: "UINT8_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2077: "JS_ARRAY_CONSTRUCTOR_TYPE",
  2078: "JS_PROMISE_CONSTRUCTOR_TYPE",
  2079: "JS_REG_EXP_CONSTRUCTOR_TYPE",
  2080: "JS_CLASS_CONSTRUCTOR_TYPE",
  2081: "JS_ARRAY_ITERATOR_PROTOTYPE_TYPE",
  2082: "JS_ITERATOR_PROTOTYPE_TYPE",
  2083: "JS_MAP_ITERATOR_PROTOTYPE_TYPE",
  2084: "JS_OBJECT_PROTOTYPE_TYPE",
  2085: "JS_PROMISE_PROTOTYPE_TYPE",
  2086: "JS_REG_EXP_PROTOTYPE_TYPE",
  2087: "JS_SET_ITERATOR_PROTOTYPE_TYPE",
  2088: "JS_SET_PROTOTYPE_TYPE",
  2089: "JS_STRING_ITERATOR_PROTOTYPE_TYPE",
  2090: "JS_TYPED_ARRAY_PROTOTYPE_TYPE",
  2091: "JS_MAP_KEY_ITERATOR_TYPE",
  2092: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  2093: "JS_MAP_VALUE_ITERATOR_TYPE",
  2094: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  2095: "JS_SET_VALUE_ITERATOR_TYPE",
  2096: "JS_GENERATOR_OBJECT_TYPE",
  2097: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  2098: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  2099: "JS_MAP_TYPE",
  2100: "JS_SET_TYPE",
  2101: "JS_WEAK_MAP_TYPE",
  2102: "JS_WEAK_SET_TYPE",
  2103: "JS_ARGUMENTS_OBJECT_TYPE",
  2104: "JS_ARRAY_TYPE",
  2105: "JS_ARRAY_ITERATOR_TYPE",
  2106: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  2107: "JS_COLLATOR_TYPE",
  2108: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  2109: "JS_DATE_TYPE",
  2110: "JS_DATE_TIME_FORMAT_TYPE",
  2111: "JS_DISPLAY_NAMES_TYPE",
  2112: "JS_ERROR_TYPE",
  2113: "JS_EXTERNAL_OBJECT_TYPE",
  2114: "JS_FINALIZATION_REGISTRY_TYPE",
  2115: "JS_LIST_FORMAT_TYPE",
  2116: "JS_LOCALE_TYPE",
  2117: "JS_MESSAGE_OBJECT_TYPE",
  2118: "JS_NUMBER_FORMAT_TYPE",
  2119: "JS_PLURAL_RULES_TYPE",
  2120: "JS_REG_EXP_TYPE",
  2121: "JS_REG_EXP_STRING_ITERATOR_TYPE",
  2122: "JS_RELATIVE_TIME_FORMAT_TYPE",
  2123: "JS_SEGMENT_ITERATOR_TYPE",
  2124: "JS_SEGMENTER_TYPE",
  2125: "JS_SEGMENTS_TYPE",
  2126: "JS_SHADOW_REALM_TYPE",
  2127: "JS_SHARED_STRUCT_TYPE",
  2128: "JS_STRING_ITERATOR_TYPE",
  2129: "JS_TEMPORAL_CALENDAR_TYPE",
  2130: "JS_TEMPORAL_DURATION_TYPE",
  2131: "JS_TEMPORAL_INSTANT_TYPE",
  2132: "JS_TEMPORAL_PLAIN_DATE_TYPE",
  2133: "JS_TEMPORAL_PLAIN_DATE_TIME_TYPE",
  2134: "JS_TEMPORAL_PLAIN_MONTH_DAY_TYPE",
  2135: "JS_TEMPORAL_PLAIN_TIME_TYPE",
  2136: "JS_TEMPORAL_PLAIN_YEAR_MONTH_TYPE",
  2137: "JS_TEMPORAL_TIME_ZONE_TYPE",
  2138: "JS_TEMPORAL_ZONED_DATE_TIME_TYPE",
  2139: "JS_V8_BREAK_ITERATOR_TYPE",
  2140: "JS_WEAK_REF_TYPE",
  2141: "WASM_GLOBAL_OBJECT_TYPE",
  2142: "WASM_INSTANCE_OBJECT_TYPE",
  2143: "WASM_MEMORY_OBJECT_TYPE",
  2144: "WASM_MODULE_OBJECT_TYPE",
  2145: "WASM_SUSPENDER_OBJECT_TYPE",
  2146: "WASM_TABLE_OBJECT_TYPE",
  2147: "WASM_TAG_OBJECT_TYPE",
  2148: "WASM_VALUE_OBJECT_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
    ("read_only_space", 0x02149): (250, "MetaMap"),
    ("read_only_space", 0x02171): (131, "NullMap"),
    ("read_only_space", 0x02199): (234, "StrongDescriptorArrayMap"),
    ("read_only_space", 0x021c1): (264, "WeakArrayListMap"),
    ("read_only_space", 0x02205): (157, "EnumCacheMap"),
    ("read_only_space", 0x02239): (179, "FixedArrayMap"),
    ("read_only_space", 0x02285): (8, "OneByteInternalizedStringMap"),
    ("read_only_space", 0x022d1): (247, "FreeSpaceMap"),
    ("read_only_space", 0x022f9): (246, "OnePointerFillerMap"),
    ("read_only_space", 0x02321): (246, "TwoPointerFillerMap"),
    ("read_only_space", 0x02349): (131, "UninitializedMap"),
    ("read_only_space", 0x023c1): (131, "UndefinedMap"),
    ("read_only_space", 0x02405): (130, "HeapNumberMap"),
    ("read_only_space", 0x02439): (131, "TheHoleMap"),
    ("read_only_space", 0x02499): (131, "BooleanMap"),
    ("read_only_space", 0x0253d): (194, "ByteArrayMap"),
    ("read_only_space", 0x02565): (179, "FixedCOWArrayMap"),
    ("read_only_space", 0x0258d): (180, "HashTableMap"),
    ("read_only_space", 0x025b5): (128, "SymbolMap"),
    ("read_only_space", 0x025dd): (40, "OneByteStringMap"),
    ("read_only_space", 0x02605): (256, "ScopeInfoMap"),
    ("read_only_space", 0x0262d): (257, "SharedFunctionInfoMap"),
    ("read_only_space", 0x02655): (240, "CodeMap"),
    ("read_only_space", 0x0267d): (239, "CellMap"),
    ("read_only_space", 0x026a5): (255, "GlobalPropertyCellMap"),
    ("read_only_space", 0x026cd): (204, "ForeignMap"),
    ("read_only_space", 0x026f5): (238, "TransitionArrayMap"),
    ("read_only_space", 0x0271d): (45, "ThinOneByteStringMap"),
    ("read_only_space", 0x02745): (245, "FeedbackVectorMap"),
    ("read_only_space", 0x0277d): (131, "ArgumentsMarkerMap"),
    ("read_only_space", 0x027dd): (131, "ExceptionMap"),
    ("read_only_space", 0x02839): (131, "TerminationExceptionMap"),
    ("read_only_space", 0x028a1): (131, "OptimizedOutMap"),
    ("read_only_space", 0x02901): (131, "StaleRegisterMap"),
    ("read_only_space", 0x02961): (193, "ScriptContextTableMap"),
    ("read_only_space", 0x02989): (191, "ClosureFeedbackCellArrayMap"),
    ("read_only_space", 0x029b1): (244, "FeedbackMetadataArrayMap"),
    ("read_only_space", 0x029d9): (179, "ArrayListMap"),
    ("read_only_space", 0x02a01): (129, "BigIntMap"),
    ("read_only_space", 0x02a29): (192, "ObjectBoilerplateDescriptionMap"),
    ("read_only_space", 0x02a51): (195, "BytecodeArrayMap"),
    ("read_only_space", 0x02a79): (241, "CodeDataContainerMap"),
    ("read_only_space", 0x02aa1): (242, "CoverageInfoMap"),
    ("read_only_space", 0x02ac9): (196, "FixedDoubleArrayMap"),
    ("read_only_space", 0x02af1): (182, "GlobalDictionaryMap"),
    ("read_only_space", 0x02b19): (159, "ManyClosuresCellMap"),
    ("read_only_space", 0x02b41): (251, "MegaDomHandlerMap"),
    ("read_only_space", 0x02b69): (179, "ModuleInfoMap"),
    ("read_only_space", 0x02b91): (183, "NameDictionaryMap"),
    ("read_only_space", 0x02bb9): (159, "NoClosuresCellMap"),
    ("read_only_space", 0x02be1): (185, "NumberDictionaryMap"),
    ("read_only_space", 0x02c09): (159, "OneClosureCellMap"),
    ("read_only_space", 0x02c31): (186, "OrderedHashMapMap"),
    ("read_only_space", 0x02c59): (187, "OrderedHashSetMap"),
    ("read_only_space", 0x02c81): (184, "NameToIndexHashTableMap"),
    ("read_only_space", 0x02ca9): (189, "RegisteredSymbolTableMap"),
    ("read_only_space", 0x02cd1): (188, "OrderedNameDictionaryMap"),
    ("read_only_space", 0x02cf9): (253, "PreparseDataMap"),
    ("read_only_space", 0x02d21): (254, "PropertyArrayMap"),
    ("read_only_space", 0x02d49): (153, "SideEffectCallHandlerInfoMap"),
    ("read_only_space", 0x02d71): (153, "SideEffectFreeCallHandlerInfoMap"),
    ("read_only_space", 0x02d99): (153, "NextCallSideEffectFreeCallHandlerInfoMap"),
    ("read_only_space", 0x02dc1): (190, "SimpleNumberDictionaryMap"),
    ("read_only_space", 0x02de9): (228, "SmallOrderedHashMapMap"),
    ("read_only_space", 0x02e11): (229, "SmallOrderedHashSetMap"),
    ("read_only_space", 0x02e39): (230, "SmallOrderedNameDictionaryMap"),
    ("read_only_space", 0x02e61): (235, "SourceTextModuleMap"),
    ("read_only_space", 0x02e89): (261, "SwissNameDictionaryMap"),
    ("read_only_space", 0x02eb1): (236, "SyntheticModuleMap"),
    ("read_only_space", 0x02ed9): (262, "WasmApiFunctionRefMap"),
    ("read_only_space", 0x02f01): (222, "WasmCapiFunctionDataMap"),
    ("read_only_space", 0x02f29): (223, "WasmExportedFunctionDataMap"),
    ("read_only_space", 0x02f51): (205, "WasmInternalFunctionMap"),
    ("read_only_space", 0x02f79): (224, "WasmJSFunctionDataMap"),
    ("read_only_space", 0x02fa1): (263, "WasmOnFulfilledDataMap"),
    ("read_only_space", 0x02fc9): (206, "WasmTypeInfoMap"),
    ("read_only_space", 0x02ff1): (237, "WeakFixedArrayMap"),
    ("read_only_space", 0x03019): (181, "EphemeronHashTableMap"),
    ("read_only_space", 0x03041): (243, "EmbedderDataArrayMap"),
    ("read_only_space", 0x03069): (265, "WeakCellMap"),
    ("read_only_space", 0x03091): (32, "StringMap"),
    ("read_only_space", 0x030b9): (41, "ConsOneByteStringMap"),
    ("read_only_space", 0x030e1): (33, "ConsStringMap"),
    ("read_only_space", 0x03109): (37, "ThinStringMap"),
    ("read_only_space", 0x03131): (35, "SlicedStringMap"),
    ("read_only_space", 0x03159): (43, "SlicedOneByteStringMap"),
    ("read_only_space", 0x03181): (34, "ExternalStringMap"),
    ("read_only_space", 0x031a9): (42, "ExternalOneByteStringMap"),
    ("read_only_space", 0x031d1): (50, "UncachedExternalStringMap"),
    ("read_only_space", 0x031f9): (0, "InternalizedStringMap"),
    ("read_only_space", 0x03221): (2, "ExternalInternalizedStringMap"),
    ("read_only_space", 0x03249): (10, "ExternalOneByteInternalizedStringMap"),
    ("read_only_space", 0x03271): (18, "UncachedExternalInternalizedStringMap"),
    ("read_only_space", 0x03299): (26, "UncachedExternalOneByteInternalizedStringMap"),
    ("read_only_space", 0x032c1): (58, "UncachedExternalOneByteStringMap"),
    ("read_only_space", 0x032e9): (104, "SharedOneByteStringMap"),
    ("read_only_space", 0x03311): (96, "SharedStringMap"),
    ("read_only_space", 0x03339): (109, "SharedThinOneByteStringMap"),
    ("read_only_space", 0x03361): (101, "SharedThinStringMap"),
    ("read_only_space", 0x03389): (96, "TwoByteSeqStringMigrationSentinelMap"),
    ("read_only_space", 0x033b1): (104, "OneByteSeqStringMigrationSentinelMap"),
    ("read_only_space", 0x033d9): (131, "SelfReferenceMarkerMap"),
    ("read_only_space", 0x03401): (131, "BasicBlockCountersMarkerMap"),
    ("read_only_space", 0x03445): (147, "ArrayBoilerplateDescriptionMap"),
    ("read_only_space", 0x03545): (161, "InterceptorInfoMap"),
    ("read_only_space", 0x06015): (132, "PromiseFulfillReactionJobTaskMap"),
    ("read_only_space", 0x0603d): (133, "PromiseRejectReactionJobTaskMap"),
    ("read_only_space", 0x06065): (134, "CallableTaskMap"),
    ("read_only_space", 0x0608d): (135, "CallbackTaskMap"),
    ("read_only_space", 0x060b5): (136, "PromiseResolveThenableJobTaskMap"),
    ("read_only_space", 0x060dd): (139, "FunctionTemplateInfoMap"),
    ("read_only_space", 0x06105): (140, "ObjectTemplateInfoMap"),
    ("read_only_space", 0x0612d): (141, "AccessCheckInfoMap"),
    ("read_only_space", 0x06155): (142, "AccessorInfoMap"),
    ("read_only_space", 0x0617d): (143, "AccessorPairMap"),
    ("read_only_space", 0x061a5): (144, "AliasedArgumentsEntryMap"),
    ("read_only_space", 0x061cd): (145, "AllocationMementoMap"),
    ("read_only_space", 0x061f5): (148, "AsmWasmDataMap"),
    ("read_only_space", 0x0621d): (149, "AsyncGeneratorRequestMap"),
    ("read_only_space", 0x06245): (150, "BreakPointMap"),
    ("read_only_space", 0x0626d): (151, "BreakPointInfoMap"),
    ("read_only_space", 0x06295): (152, "CachedTemplateObjectMap"),
    ("read_only_space", 0x062bd): (154, "CallSiteInfoMap"),
    ("read_only_space", 0x062e5): (155, "ClassPositionsMap"),
    ("read_only_space", 0x0630d): (156, "DebugInfoMap"),
    ("read_only_space", 0x06335): (158, "ErrorStackDataMap"),
    ("read_only_space", 0x0635d): (160, "FunctionTemplateRareDataMap"),
    ("read_only_space", 0x06385): (162, "InterpreterDataMap"),
    ("read_only_space", 0x063ad): (163, "ModuleRequestMap"),
    ("read_only_space", 0x063d5): (164, "PromiseCapabilityMap"),
    ("read_only_space", 0x063fd): (165, "PromiseOnStackMap"),
    ("read_only_space", 0x06425): (166, "PromiseReactionMap"),
    ("read_only_space", 0x0644d): (167, "PropertyDescriptorObjectMap"),
    ("read_only_space", 0x06475): (168, "PrototypeInfoMap"),
    ("read_only_space", 0x0649d): (169, "RegExpBoilerplateDescriptionMap"),
    ("read_only_space", 0x064c5): (170, "ScriptMap"),
    ("read_only_space", 0x064ed): (171, "ScriptOrModuleMap"),
    ("read_only_space", 0x06515): (172, "SourceTextModuleInfoEntryMap"),
    ("read_only_space", 0x0653d): (173, "StackFrameInfoMap"),
    ("read_only_space", 0x06565): (174, "TemplateObjectDescriptionMap"),
    ("read_only_space", 0x0658d): (175, "Tuple2Map"),
    ("read_only_space", 0x065b5): (176, "WasmContinuationObjectMap"),
    ("read_only_space", 0x065dd): (177, "WasmExceptionTagMap"),
    ("read_only_space", 0x06605): (178, "WasmIndirectFunctionTableMap"),
    ("read_only_space", 0x0662d): (198, "SloppyArgumentsElementsMap"),
    ("read_only_space", 0x06655): (233, "DescriptorArrayMap"),
    ("read_only_space", 0x0667d): (219, "UncompiledDataWithoutPreparseDataMap"),
    ("read_only_space", 0x066a5): (217, "UncompiledDataWithPreparseDataMap"),
    ("read_only_space", 0x066cd): (220, "UncompiledDataWithoutPreparseDataWithJobMap"),
    ("read_only_space", 0x066f5): (218, "UncompiledDataWithPreparseDataAndJobMap"),
    ("read_only_space", 0x0671d): (252, "OnHeapBasicBlockProfilerDataMap"),
    ("read_only_space", 0x06745): (199, "TurbofanBitsetTypeMap"),
    ("read_only_space", 0x0676d): (203, "TurbofanUnionTypeMap"),
    ("read_only_space", 0x06795): (202, "TurbofanRangeTypeMap"),
    ("read_only_space", 0x067bd): (200, "TurbofanHeapConstantTypeMap"),
    ("read_only_space", 0x067e5): (201, "TurbofanOtherNumberConstantTypeMap"),
    ("read_only_space", 0x0680d): (248, "InternalClassMap"),
    ("read_only_space", 0x06835): (259, "SmiPairMap"),
    ("read_only_space", 0x0685d): (258, "SmiBoxMap"),
    ("read_only_space", 0x06885): (225, "ExportedSubClassBaseMap"),
    ("read_only_space", 0x068ad): (226, "ExportedSubClassMap"),
    ("read_only_space", 0x068d5): (231, "AbstractInternalClassSubclass1Map"),
    ("read_only_space", 0x068fd): (232, "AbstractInternalClassSubclass2Map"),
    ("read_only_space", 0x06925): (197, "InternalClassWithSmiElementsMap"),
    ("read_only_space", 0x0694d): (249, "InternalClassWithStructElementsMap"),
    ("read_only_space", 0x06975): (227, "ExportedSubClass2Map"),
    ("read_only_space", 0x0699d): (260, "SortStateMap"),
    ("read_only_space", 0x069c5): (146, "AllocationSiteWithWeakNextMap"),
    ("read_only_space", 0x069ed): (146, "AllocationSiteWithoutWeakNextMap"),
    ("read_only_space", 0x06a15): (137, "LoadHandler1Map"),
    ("read_only_space", 0x06a3d): (137, "LoadHandler2Map"),
    ("read_only_space", 0x06a65): (137, "LoadHandler3Map"),
    ("read_only_space", 0x06a8d): (138, "StoreHandler0Map"),
    ("read_only_space", 0x06ab5): (138, "StoreHandler1Map"),
    ("read_only_space", 0x06add): (138, "StoreHandler2Map"),
    ("read_only_space", 0x06b05): (138, "StoreHandler3Map"),
    ("map_space", 0x02149): (2113, "ExternalMap"),
    ("map_space", 0x02171): (2117, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x021e9): "EmptyWeakArrayList",
  ("read_only_space", 0x021f5): "EmptyDescriptorArray",
  ("read_only_space", 0x0222d): "EmptyEnumCache",
  ("read_only_space", 0x02261): "EmptyFixedArray",
  ("read_only_space", 0x02269): "NullValue",
  ("read_only_space", 0x02371): "UninitializedValue",
  ("read_only_space", 0x023e9): "UndefinedValue",
  ("read_only_space", 0x0242d): "NanValue",
  ("read_only_space", 0x02461): "TheHoleValue",
  ("read_only_space", 0x0248d): "HoleNanValue",
  ("read_only_space", 0x024c1): "TrueValue",
  ("read_only_space", 0x02501): "FalseValue",
  ("read_only_space", 0x02531): "empty_string",
  ("read_only_space", 0x0276d): "EmptyScopeInfo",
  ("read_only_space", 0x027a5): "ArgumentsMarker",
  ("read_only_space", 0x02805): "Exception",
  ("read_only_space", 0x02861): "TerminationException",
  ("read_only_space", 0x028c9): "OptimizedOut",
  ("read_only_space", 0x02929): "StaleRegister",
  ("read_only_space", 0x03429): "EmptyPropertyArray",
  ("read_only_space", 0x03431): "EmptyByteArray",
  ("read_only_space", 0x03439): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x0346d): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x03479): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x03481): "EmptySlowElementDictionary",
  ("read_only_space", 0x034a5): "EmptyOrderedHashMap",
  ("read_only_space", 0x034b9): "EmptyOrderedHashSet",
  ("read_only_space", 0x034cd): "EmptyFeedbackMetadata",
  ("read_only_space", 0x034d9): "EmptyPropertyDictionary",
  ("read_only_space", 0x03501): "EmptyOrderedPropertyDictionary",
  ("read_only_space", 0x03519): "EmptySwissPropertyDictionary",
  ("read_only_space", 0x0356d): "NoOpInterceptorInfo",
  ("read_only_space", 0x03595): "EmptyArrayList",
  ("read_only_space", 0x035a1): "EmptyWeakFixedArray",
  ("read_only_space", 0x035a9): "InfinityValue",
  ("read_only_space", 0x035b5): "MinusZeroValue",
  ("read_only_space", 0x035c1): "MinusInfinityValue",
  ("read_only_space", 0x035cd): "SelfReferenceMarker",
  ("read_only_space", 0x0360d): "BasicBlockCountersMarker",
  ("read_only_space", 0x03651): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x0365d): "GlobalThisBindingScopeInfo",
  ("read_only_space", 0x0368d): "EmptyFunctionScopeInfo",
  ("read_only_space", 0x036b1): "NativeScopeInfo",
  ("read_only_space", 0x036c9): "HashSeed",
  ("old_space", 0x04215): "ArgumentsIteratorAccessor",
  ("old_space", 0x04259): "ArrayLengthAccessor",
  ("old_space", 0x0429d): "BoundFunctionLengthAccessor",
  ("old_space", 0x042e1): "BoundFunctionNameAccessor",
  ("old_space", 0x04325): "ErrorStackAccessor",
  ("old_space", 0x04369): "FunctionArgumentsAccessor",
  ("old_space", 0x043ad): "FunctionCallerAccessor",
  ("old_space", 0x043f1): "FunctionNameAccessor",
  ("old_space", 0x04435): "FunctionLengthAccessor",
  ("old_space", 0x04479): "FunctionPrototypeAccessor",
  ("old_space", 0x044bd): "StringLengthAccessor",
  ("old_space", 0x04501): "WrappedFunctionLengthAccessor",
  ("old_space", 0x04545): "WrappedFunctionNameAccessor",
  ("old_space", 0x04589): "InvalidPrototypeValidityCell",
  ("old_space", 0x04591): "EmptyScript",
  ("old_space", 0x045d1): "ManyClosuresCell",
  ("old_space", 0x045dd): "ArrayConstructorProtector",
  ("old_space", 0x045f1): "NoElementsProtector",
  ("old_space", 0x04605): "MegaDOMProtector",
  ("old_space", 0x04619): "IsConcatSpreadableProtector",
  ("old_space", 0x0462d): "ArraySpeciesProtector",
  ("old_space", 0x04641): "TypedArraySpeciesProtector",
  ("old_space", 0x04655): "PromiseSpeciesProtector",
  ("old_space", 0x04669): "RegExpSpeciesProtector",
  ("old_space", 0x0467d): "StringLengthProtector",
  ("old_space", 0x04691): "ArrayIteratorProtector",
  ("old_space", 0x046a5): "ArrayBufferDetachingProtector",
  ("old_space", 0x046b9): "PromiseHookProtector",
  ("old_space", 0x046cd): "PromiseResolveProtector",
  ("old_space", 0x046e1): "MapIteratorProtector",
  ("old_space", 0x046f5): "PromiseThenProtector",
  ("old_space", 0x04709): "SetIteratorProtector",
  ("old_space", 0x0471d): "StringIteratorProtector",
  ("old_space", 0x04731): "SingleCharacterStringCache",
  ("old_space", 0x04b39): "StringSplitCache",
  ("old_space", 0x04f41): "RegExpMultipleCache",
  ("old_space", 0x05349): "BuiltinsConstantsTable",
  ("old_space", 0x05779): "AsyncFunctionAwaitRejectSharedFun",
  ("old_space", 0x0579d): "AsyncFunctionAwaitResolveSharedFun",
  ("old_space", 0x057c1): "AsyncGeneratorAwaitRejectSharedFun",
  ("old_space", 0x057e5): "AsyncGeneratorAwaitResolveSharedFun",
  ("old_space", 0x05809): "AsyncGeneratorYieldResolveSharedFun",
  ("old_space", 0x0582d): "AsyncGeneratorReturnResolveSharedFun",
  ("old_space", 0x05851): "AsyncGeneratorReturnClosedRejectSharedFun",
  ("old_space", 0x05875): "AsyncGeneratorReturnClosedResolveSharedFun",
  ("old_space", 0x05899): "AsyncIteratorValueUnwrapSharedFun",
  ("old_space", 0x058bd): "PromiseAllResolveElementSharedFun",
  ("old_space", 0x058e1): "PromiseAllSettledResolveElementSharedFun",
  ("old_space", 0x05905): "PromiseAllSettledRejectElementSharedFun",
  ("old_space", 0x05929): "PromiseAnyRejectElementSharedFun",
  ("old_space", 0x0594d): "PromiseCapabilityDefaultRejectSharedFun",
  ("old_space", 0x05971): "PromiseCapabilityDefaultResolveSharedFun",
  ("old_space", 0x05995): "PromiseCatchFinallySharedFun",
  ("old_space", 0x059b9): "PromiseGetCapabilitiesExecutorSharedFun",
  ("old_space", 0x059dd): "PromiseThenFinallySharedFun",
  ("old_space", 0x05a01): "PromiseThrowerFinallySharedFun",
  ("old_space", 0x05a25): "PromiseValueThunkFinallySharedFun",
  ("old_space", 0x05a49): "ProxyRevokeSharedFun",
}

# Lower 32 bits of first page addresses for various heap spaces.
HEAP_FIRST_PAGES = {
  0x000c0000: "old_space",
  0x00100000: "map_space",
  0x00000000: "read_only_space",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "WASM",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "STACK_SWITCH",
  "WASM_DEBUG_BREAK",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "BASELINE",
  "OPTIMIZED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
