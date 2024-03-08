//! Main data structure used to describe an index

use std::fmt;

use serde::{Deserialize, Serialize};

use crate::base::{DocId, ImpactValue, TermIndex};

use super::TermImpact;

#[derive(Serialize, Deserialize)]
pub struct TermIndexPageInformation {
    /// Position for the document ID stream
    pub docid_position: u64,

    /// Position for the impact value stream
    pub value_position: u64,

    /// Number of records
    pub length: usize,

    /// Maximum value for this page
    pub max_value: ImpactValue,

    /// Maximum document ID for this page
    pub max_doc_id: DocId,

    // /// Minimum document ID for this page
    // pub min_doc_id: DocId
}

impl TermIndexPageInformation {
    pub fn new() -> Self {
        Self {
            docid_position: 0,
            value_position: 0,
            length: 0,
            max_value: 0.,
            max_doc_id: 0,
            // min_doc_id: 0
        }
    }
}


impl std::fmt::Display for TermIndexPageInformation {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "(pos: {}/{}, len: {}, max_v: {}, max_docid: {})", 
            self.docid_position, self.value_position, self.length,
            self.max_value, self.max_doc_id
        )
    }
}

#[derive(Serialize, Deserialize)]
pub struct TermIndexInformation {
    pub pages: Vec<TermIndexPageInformation>,
    pub max_value: ImpactValue,
    pub max_doc_id: DocId,
    pub length: usize,
}

/// Global information on the index structure
#[derive(Serialize, Deserialize)]
pub struct IndexInformation {
    pub terms: Vec<TermIndexInformation>,
}

impl IndexInformation {
    /// Creates a new index information
    pub fn new() -> IndexInformation {
        IndexInformation { terms: Vec::new() }
    }
}

/// Generic trait for block-based term impact iterators
pub trait BlockTermImpactIterator : Send {
    /// Moves to the next document whose id is greater or equal than doc_id
    /// The move can be "shallow", i.e. no need to actually hold a record:
    /// this is used by the BMW algorithm
    fn next_min_doc_id(&mut self, doc_id: DocId) -> bool;

    /// Returns the current term impact (can panic)
    fn current(&self) -> TermImpact;

    /// Returns the term maximum impact
    fn max_value(&self) -> ImpactValue;

    /// Returns the maximum and minimum document ID
    fn max_doc_id(&self) -> DocId;

    /// Max block document ID (by default, returns the maximum over all impacts)
    fn max_block_value(&self) -> ImpactValue {
        // If just one block...
        self.max_value()
    }

    /// Returns the minimum document ID for this block
    fn min_block_doc_id(&self) -> DocId {
        0
    }

    /// Max block document ID (by default, returns the maximum over all impacts)
    fn max_block_doc_id(&self) -> DocId {
        // If just one block...
        self.max_doc_id()
    }

    /// Returns the total number of records
    fn length(&self) -> usize;

    /// Returns the next element
    fn next(&mut self) -> Option<TermImpact> {
        if self.next_min_doc_id(0) {
            Some(self.current())
        } else {
            None
        }
    }
}

pub trait BlockTermImpactIndex {
    /// Returns an iterator for a given term
    ///
    /// ## Arguments
    ///
    /// * `term_ix` The index of the term
    fn iterator(&self, term_ix: TermIndex) -> Box<dyn BlockTermImpactIterator + '_>;

    /// Returns all the iterators for a term (if split list)
    fn iterators(&self, term_ix: TermIndex) -> Vec<Box<dyn BlockTermImpactIterator + '_>> {
        let mut v = Vec::new();
        v.push(self.iterator(term_ix));
        v
    }

    /// Returns the number of terms in the index
    fn length(&self) -> usize;
}

pub struct ValueIterator<'a> {
    iterator: Box<dyn BlockTermImpactIterator + 'a>,
}

impl<'a> Iterator for ValueIterator<'a> {
    type Item = ImpactValue;

    fn next(&mut self) -> Option<ImpactValue> {
        if let Some(ti) = self.iterator.next() {
            Some(ti.value)
        } else {
            None
        }
    }

    fn max(self) -> Option<Self::Item> {
        return Some(self.iterator.max_value());
    }
}

struct DocIdIterator<'a> {
    iterator: Box<dyn BlockTermImpactIterator + 'a>,
}
impl<'a> Iterator for DocIdIterator<'a> {
    type Item = DocId;

    fn next(&mut self) -> Option<DocId> {
        if let Some(ti) = self.iterator.next() {
            Some(ti.docid)
        } else {
            None
        }
    }

    fn max(self) -> Option<Self::Item> {
        return Some(self.iterator.max_doc_id());
    }
}
