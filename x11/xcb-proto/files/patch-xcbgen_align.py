Obtained from:

https://cgit.freedesktop.org/xcb/proto/commit/xcbgen/align.py?id=ea7a3ac6c658164690e0febb55f4467cb9e0bcac

--- xcbgen/align.py.orig	2016-05-01 07:44:48 UTC
+++ xcbgen/align.py
@@ -16,12 +16,12 @@ class Alignment(object):
         return self.align == other.align and self.offset == other.offset
 
     def __str__(self):
-	return "(align=%d, offset=%d)" % (self.align, self.offset)
+        return "(align=%d, offset=%d)" % (self.align, self.offset)
 
     @staticmethod
     def for_primitive_type(size):
-	# compute the required start_alignment based on the size of the type
-	if size % 8 == 0:
+        # compute the required start_alignment based on the size of the type
+        if size % 8 == 0:
             # do 8-byte primitives require 8-byte alignment in X11?
             return Alignment(8,0)
         elif size % 4 == 0:
@@ -33,7 +33,7 @@ class Alignment(object):
 
 
     def align_after_fixed_size(self, size):
-	new_offset = (self.offset + size) % self.align
+        new_offset = (self.offset + size) % self.align
         return Alignment(self.align, new_offset)
 
 
@@ -41,7 +41,7 @@ class Alignment(object):
         '''
         Assuming the given external_align, checks whether
         self is fulfilled for all cases.
-	Returns True if yes, False otherwise.
+        Returns True if yes, False otherwise.
         '''
         if self.align == 1 and self.offset == 0:
             # alignment 1 with offset 0 is always fulfilled
@@ -55,9 +55,9 @@ class Alignment(object):
             # the external align guarantees less alignment -> not guaranteed
             return False
 
-	if external_align.align % self.align != 0:
+        if external_align.align % self.align != 0:
             # the external align cannot be divided by our align
-	    # -> not guaranteed
+            # -> not guaranteed
             # (this can only happen if there are alignments that are not
             # a power of 2, which is highly discouraged. But better be
             # safe and check for it)
@@ -72,7 +72,7 @@ class Alignment(object):
 
     def combine_with(self, other):
         # returns the alignment that is guaranteed when
-	# both, self or other, can happen
+        # both, self or other, can happen
         new_align = gcd(self.align, other.align)
         new_offset_candidate1 = self.offset % new_align
         new_offset_candidate2 = other.offset % new_align
@@ -83,8 +83,8 @@ class Alignment(object):
             new_align = gcd(new_align, offset_diff)
             new_offset_candidate1 = self.offset % new_align
             new_offset_candidate2 = other.offset % new_align
-	    assert new_offset_candidate1 == new_offset_candidate2
-	    new_offset = new_offset_candidate1
+            assert new_offset_candidate1 == new_offset_candidate2
+            new_offset = new_offset_candidate1
         # return the result
         return Alignment(new_align, new_offset)
 
@@ -92,44 +92,44 @@ class Alignment(object):
 class AlignmentLog(object):
 
     def __init__(self):
-	self.ok_list = []
-	self.fail_list = []
-	self.verbosity = 1
+        self.ok_list = []
+        self.fail_list = []
+        self.verbosity = 1
 
     def __str__(self):
-	result = ""
+        result = ""
 
-	# output the OK-list
-	for (align_before, field_name, type_obj, callstack, align_after) in self.ok_list:
-	    stacksize = len(callstack)
+        # output the OK-list
+        for (align_before, field_name, type_obj, callstack, align_after) in self.ok_list:
+            stacksize = len(callstack)
             indent = '  ' * stacksize
-	    if self.ok_callstack_is_relevant(callstack):
+            if self.ok_callstack_is_relevant(callstack):
                 if field_name is None or field_name == "":
-	            result += ("    %sok: %s:\n\t%sbefore: %s, after: %s\n"
-		        % (indent, str(type_obj), indent, str(align_before), str(align_after)))
-	        else:
-		    result += ("    %sok: field \"%s\" in %s:\n\t%sbefore: %s, after: %s\n"
-		        % (indent, str(field_name), str(type_obj),
-		           indent, str(align_before), str(align_after)))
+                    result += ("    %sok: %s:\n\t%sbefore: %s, after: %s\n"
+                        % (indent, str(type_obj), indent, str(align_before), str(align_after)))
+                else:
+                    result += ("    %sok: field \"%s\" in %s:\n\t%sbefore: %s, after: %s\n"
+                        % (indent, str(field_name), str(type_obj),
+                           indent, str(align_before), str(align_after)))
                 if self.verbosity >= 1:
-		    result += self.callstack_to_str(indent, callstack)
+                    result += self.callstack_to_str(indent, callstack)
 
-	# output the fail-list
-	for (align_before, field_name, type_obj, callstack, reason) in self.fail_list:
-	    stacksize = len(callstack)
+        # output the fail-list
+        for (align_before, field_name, type_obj, callstack, reason) in self.fail_list:
+            stacksize = len(callstack)
             indent = '  ' * stacksize
-	    if field_name is None or field_name == "":
-	        result += ("    %sfail: align %s is incompatible with\n\t%s%s\n\t%sReason: %s\n"
-		    % (indent, str(align_before), indent, str(type_obj), indent, reason))
-	    else:
-		result += ("    %sfail: align %s is incompatible with\n\t%sfield \"%s\" in %s\n\t%sReason: %s\n"
-		    % (indent, str(align_before), indent, str(field_name), str(type_obj), indent, reason))
+            if field_name is None or field_name == "":
+                result += ("    %sfail: align %s is incompatible with\n\t%s%s\n\t%sReason: %s\n"
+                    % (indent, str(align_before), indent, str(type_obj), indent, reason))
+            else:
+                result += ("    %sfail: align %s is incompatible with\n\t%sfield \"%s\" in %s\n\t%sReason: %s\n"
+                    % (indent, str(align_before), indent, str(field_name), str(type_obj), indent, reason))
 
             if self.verbosity >= 1:
-	        result += self.callstack_to_str(indent, callstack)
+                result += self.callstack_to_str(indent, callstack)
 
 
-	return result
+        return result
 
 
     def callstack_to_str(self, indent, callstack):
@@ -137,41 +137,41 @@ class AlignmentLog(object):
         for stack_elem in callstack:
             result += "\t  %s%s\n" % (indent, str(stack_elem))
         result += "\t%s]\n" % indent
-	return result
+        return result
 
 
     def ok_callstack_is_relevant(self, ok_callstack):
         # determine whether an ok callstack is relevant for logging
-	if self.verbosity >= 2:
-	    return True
+        if self.verbosity >= 2:
+            return True
 
         # empty callstacks are always relevant
-	if len(ok_callstack) == 0:
+        if len(ok_callstack) == 0:
             return True
 
-	# check whether the ok_callstack is a subset or equal to a fail_callstack
+        # check whether the ok_callstack is a subset or equal to a fail_callstack
         for (align_before, field_name, type_obj, fail_callstack, reason) in self.fail_list:
             if len(ok_callstack) <= len(fail_callstack):
                 zipped = zip(ok_callstack, fail_callstack[:len(ok_callstack)])
-		is_subset = all([i == j for i, j in zipped])
-		if is_subset:
+                is_subset = all([i == j for i, j in zipped])
+                if is_subset:
                     return True
 
         return False
 
 
     def ok(self, align_before, field_name, type_obj, callstack, align_after):
-	self.ok_list.append((align_before, field_name, type_obj, callstack, align_after))
+        self.ok_list.append((align_before, field_name, type_obj, callstack, align_after))
 
     def fail(self, align_before, field_name, type_obj, callstack, reason):
-	self.fail_list.append((align_before, field_name, type_obj, callstack, reason))
+        self.fail_list.append((align_before, field_name, type_obj, callstack, reason))
 
     def append(self, other):
-	self.ok_list.extend(other.ok_list)
-	self.fail_list.extend(other.fail_list)
+        self.ok_list.extend(other.ok_list)
+        self.fail_list.extend(other.fail_list)
 
     def ok_count(self):
-	return len(self.ok_list)
+        return len(self.ok_list)
 
 
 
